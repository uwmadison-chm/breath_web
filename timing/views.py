import json
import datetime
import csv

from django.template import RequestContext 
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, QueryDict
from django.core.urlresolvers import reverse
from django.db import IntegrityError

from timing.models import Experiment, Participant, Run, Response, Viewing
from timing import forms


def welcome_consent(request, slug):
    exp = get_object_or_404(Experiment, url_slug=slug)
    if request.method == "GET":
        request.session.flush()
    request.session.set_expiry(0)
    __add_log_item('welcome_consent', request)
    form = forms.ConsentForm()
    if request.method == "POST":
        form = forms.ConsentForm(request.POST)
        if form.is_valid():
            request.session['consent'] = form.cleaned_data.get('consent')
            return redirect(login, slug=exp.url_slug)
    return render_to_response('welcome_consent.html',
        {'form': form, 'exp': exp}, context_instance=RequestContext(request))


def background(request, slug):
    exp = get_object_or_404(Experiment, url_slug=slug)
    return render_to_response('background.html',
        {'exp': exp}, context_instance=RequestContext(request))


def privacy(request, slug):
    exp = get_object_or_404(Experiment, url_slug=slug)
    return render_to_response('privacy.html',
        {'exp': exp}, context_instance=RequestContext(request))


def login(request, slug):
    exp = get_object_or_404(Experiment, url_slug=slug)
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            try:
                ppt = Participant.objects.get(
                    email=form.cleaned_data['email'])
            except Participant.DoesNotExist:
                ppt = Participant(
                    email=form.cleaned_data['email'],
                    consent_given=request.session.get('consent'))
                ppt.save()
            request.session['ppt_id'] = ppt.pk
            if not ppt.has_demographics:
                # We can't skip demographics...
                return redirect(demographics, slug=exp.url_slug)
            if ppt.has_run_data:
                # We can skip instructions and practice
                return redirect(run_task, slug=exp.url_slug)

            # The fall-through is to go through instructions
            return redirect(instructions, slug=exp.url_slug)
    else:
        form = forms.LoginForm()
    __add_log_item('login_form', request)
    return render_to_response('login.html', 
        {'form': form, 'exp': exp}, context_instance=RequestContext(request))


def demographics(request, slug):
    exp = get_object_or_404(Experiment, url_slug=slug)
    ppt = get_object_or_404(Participant, pk=request.session['ppt_id'])
    __add_log_item('demographics_form', request, ppt)
    form = forms.DemographicsForm(instance=ppt)
    if request.method == "POST":
        form = forms.DemographicsForm(request.POST, instance=ppt)
        try:
            form.save()
            __add_log_item('demographics_save_success', request, ppt)
            return redirect(instructions, slug=exp.url_slug)
        except Exception as e:
            __add_log_item('demographics_save_fail', request, ppt)
            print e
            print ppt.__dict__
            print form.errors

    return render_to_response('demographics.html', 
        {'form': form, 'exp': exp}, context_instance=RequestContext(request))


def instructions(request, slug):
    exp = get_object_or_404(Experiment, url_slug=slug)
    ppt = get_object_or_404(Participant, pk=request.session['ppt_id'])
    __add_log_item('instructions', request, ppt)
    return render_to_response('instructions.html',
        {'exp': exp}, context_instance=RequestContext(request))


def guided_practice(request, slug):
    exp = get_object_or_404(Experiment, url_slug=slug)
    ppt = get_object_or_404(Participant, pk=request.session['ppt_id'])
    __add_log_item('guided_practice', request, ppt)
    return render_to_response('guided_practice.html',
        {'exp': exp}, context_instance=RequestContext(request))


def practice(request, slug):
    exp = get_object_or_404(Experiment, url_slug=slug)
    ppt = get_object_or_404(Participant, pk=request.session['ppt_id'])
    __add_log_item('practice', request, ppt)
    return render_to_response('practice.html',
        {'exp': exp}, context_instance=RequestContext(request))


def run_swf(request, slug):
    exp = get_object_or_404(Experiment, url_slug=slug)
    ppt_key = request.session.get('ppt_id')
    ppt = get_object_or_404(Participant, pk=ppt_key)
    run = exp.run_set.create(
        participant=ppt, 
        user_agent=request.META['HTTP_USER_AGENT'])
    flash_params = {
        'post_path': reverse(thanks, kwargs={'slug': exp.url_slug}),
        'finish_path': reverse(run_task, kwargs={'slug': exp.url_slug}),
        'breath_time_key': exp.breath_time_key,
        'run_start_key': exp.breath_time_key,
        'end_cycle_key': exp.end_cycle_key,
        'cycle_length': exp.cycle_length,
        'ppt_id': ppt.pk,
        'run_id': run.pk,}
    qd = QueryDict('').copy()
    qd.update(flash_params)
    return render_to_response('run_swf.html', {
        'run': run,
        'exp': exp,
        'participant': ppt,
        'flash_params': qd.urlencode()})


def run_task(request, slug):
    exp = get_object_or_404(Experiment, url_slug=slug)

    ppt_key = (request.session.get('ppt_id') or 
        request.POST['ppt_id'])
    ppt = get_object_or_404(Participant, pk=ppt_key)
    if request.method == "GET":
        if exp.use_swf_url is not None:
            # We're replacing the regular game with the Flash game
            return redirect(run_swf, slug=exp.url_slug)

        __add_log_item('run_task', request, ppt)
        run = exp.run_set.create(
            participant=ppt, 
            user_agent=request.META['HTTP_USER_AGENT'])
        request.session['run_id'] = run.pk
        return render_to_response('run_task.html', {
            'run': run,
            'exp': exp},
            context_instance=RequestContext(request))

    if request.method == "POST":
        run_key = request.session.get('run_id') or request.POST['run_id']
        run = Run.objects.get(pk=run_key)
        return_data = {'finish': False}
        cur_time = datetime.datetime.utcnow()
        if run.started_at is None:
            run.start()
            run.save()
        saved_nums = []
        save_queue = json.loads(request.POST['save_queue'])
        for num, data in save_queue.iteritems():
            try:
                resp = run.response_set.create(
                    press_num=data['num'], 
                    key=data['key'],
                    prompt_type = data['prompt'],
                    ms_since_run_start=data['since_run_start'],
                    duration_ms=data['duration'],
                    timezone_offset_min=data['timezone_offset_min'],
                    played_error_chime=data['chimed'])
            except IntegrityError:
                pass
            saved_nums.append(data['num'])

        target_tdelta = datetime.timedelta(seconds=exp.run_length_seconds)
        run_tdelta = cur_time - run.started_at
        if run_tdelta > target_tdelta:
            return_data['finish'] = True
            run.finished_at = cur_time
            run.save()

        return_data['saved_nums'] = saved_nums
        return HttpResponse(json.dumps(return_data))


def thanks(request, slug):
    exp = get_object_or_404(Experiment, url_slug=slug)
    ppt = get_object_or_404(Participant, pk=request.session['ppt_id'])
    __add_log_item('run_task', request, ppt)

    return render_to_response('thanks.html', {
        'participant': ppt,
        'exp': exp}, context_instance=RequestContext(request))


def log(request, view_key, slug):
    exp = get_object_or_404(Experiment, url_slug=slug)
    ppt = get_object_or_404(Participant, pk=request.session['ppt_id'])
    __add_log_item(view_key, request, ppt)
    return HttpResponse('')


def run_csv(request, run_id):
    print("foo")
    run = get_object_or_404(Run, pk=run_id)
    header = [
        'participant_number',
        'experiment_number',
        'run_number',
        'run_finished',
        'keypress_number',
        'keycode',
        'ms_since_run_start',
        'duration_ms',
        'server_timestamp_sec',
        'timezone_offset_sec',
        'played_chime']
    response = HttpResponse(mimetype='text/plain')
    writer = csv.writer(response)
    writer.writerow(header)
    for resp in run.response_set.order_by('press_num'):
        row = [getattr(resp, att) for att in header]
        writer.writerow(row)
    return response

def __add_log_item(view_key, request, ppt=None):
    sk = request.session._session_key
    v = Viewing(view_key=view_key, session_key=sk, participant=ppt)
    v.save()
