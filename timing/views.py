import json

from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse

def welcome_consent(request):
    return render_to_response('welcome_consent.html')

def demographics(request):
    return render_to_response('demographics.html')

def login(request):
    return render_to_response('login.html')

def instructions(request):
    return render_to_response('instructions.html')

def practice(request):
    return render_to_response('practice.html')

def run_task(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({"result": "ok"}))
    else:
        return render_to_response('run_task.html')

def thanks(request):
    return render_to_response('thanks.html')


