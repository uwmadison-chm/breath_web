import json
import datetime

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponse
from django.db import IntegrityError

from timing.models import Participant, Run, Response, Viewing
from timing import forms

def welcome_consent(request):
    request.session.set_expiry(0)
    __add_log_item('welcome_consent', request)
    form = forms.ConsentForm()
    if request.method == "POST":
        form = forms.ConsentForm(request.POST)
        if form.is_valid():
            request.session['consent'] = form.cleaned_data.get('consent')
            return redirect(login)
    return render_to_response('welcome_consent.html', {'form' : form})        

def login(request):
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
            if ppt.has_demographics:
                return redirect(instructions)
            else:
                return redirect(demographics)
    else:
        form = forms.LoginForm()
    __add_log_item('login_form', request)
    return render_to_response('login.html', {'form' : form})
            
def demographics(request):
    ppt = get_object_or_404(Participant, pk=request.session['ppt_id'])
    __add_log_item('demographics_form', request, ppt)
    form = forms.DemographicsForm(instance=ppt)
    if request.method == "POST":
        form = forms.DemographicsForm(request.POST, instance=ppt)
        try:
            form.save()
            __add_log_item('demographics_save_success', request, ppt)
            return redirect(instructions)
        except Exception as e:
            __add_log_item('demographics_save_fail', request, ppt)
            print e
            print ppt.__dict__
            print form.errors
    
    return render_to_response('demographics.html', {'form' : form})

def instructions(request):
    ppt = get_object_or_404(Participant, pk=request.session['ppt_id'])
    __add_log_item('instructions', request, ppt)
    return render_to_response('instructions.html')

def guided_practice(request):
    ppt = get_object_or_404(Participant, pk=request.session['ppt_id'])
    __add_log_item('guided_practice', request, ppt)
    return render_to_response('guided_practice.html')

def practice(request):
    ppt = get_object_or_404(Participant, pk=request.session['ppt_id'])
    __add_log_item('practice', request, ppt)
    return render_to_response('practice.html')

def run_task(request):
    ppt = get_object_or_404(Participant, pk=request.session['ppt_id'])
    __add_log_item('run_task', request, ppt)
    if request.method == "GET":
        run = Run(participant=ppt)
        run.save()
        request.session['run_id'] = run.pk
        return render_to_response('run_task.html', {
            'run' : run,
            'task_len_min' : (run.planned_length_sec / 60)
        })
        
    if request.method == "POST":
        run = Run.objects.get(pk=request.session['run_id'])
        return_data = {'finish' : False}
        if run.started_at is None:
            run.start()
            run.save()
        saved_nums = []
        save_queue = json.loads(request.POST['save_queue'])
        for num, data in save_queue.iteritems():
            try:
                resp = Response(
                    run=run, press_num=data['num'], key=data['key'], 
                    ms_since_run_start=data['time'])
                resp.save()
            except IntegrityError:
                pass
            saved_nums.append(data['num'])
        
        target_tdelta = datetime.timedelta(seconds=run.planned_length_sec)
        run_tdelta = cur_time - run.started_at
        if run_tdelta > target_tdelta:
            return_data['finish'] = True
            run.finished_at = cur_time
            run.save()
            
        return_data['saved_nums'] = saved_nums
        return HttpResponse(json.dumps(return_data))
                
def thanks(request):
    ppt = get_object_or_404(Participant, pk=request.session['ppt_id'])
    __add_log_item('run_task', request, ppt)
    
    return render_to_response('thanks.html', {
        'participant' : ppt
    })

def log(request, view_key):
    ppt = get_object_or_404(Participant, pk=request.session['ppt_id'])
    __add_log_item(view_key, request, ppt)
    return HttpResponse('')

def __add_log_item(view_key, request, ppt=None):
    sk = request.session._session_key
    v = Viewing(view_key=view_key, session_key=sk, participant=ppt)
    v.save()