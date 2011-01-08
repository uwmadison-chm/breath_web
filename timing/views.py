from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from models import Run
import re, datetime

import csv
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def login(request):
    msg = ""
    if request.method == 'POST':
        user = request.POST['user']
        return render_to_response('timing/instructions.html', {'user':user})
    else:
        return render_to_response('timing/login.html')

def instructions(request):
    if request.method == 'POST':
        username = request.POST['name']
    else:
        username = 'default'
        
    return render_to_response('timing/instructions.html', {'user':username})

def practice(request):
    if request.method == 'POST':
        user = request.POST['user']
        return render_to_response('timing/practice.html', {'user':user})
    else:
        return redirect('/apps/meditime/instructions/')

def run(request):
    if request.method == 'POST':
        user = request.POST['user']
        return render_to_response('timing/timing.html', {'user':user})
    else:
        return redirect('/instructions/')

def submit(request):
    if request.method == 'POST':
        username = request.POST['user']
        timing = request.POST['timing']

        timelist = re.findall(r'\d+', timing)
        newrun = Run(user=username, date=datetime.datetime.now(), keypresses=timing)
        newrun.save()
        
        saveloc = '/home/benedict/coding/research/meditime/output/' + username + str(datetime.datetime.now())
        f = open(saveloc, 'w')
        f.write(timing)
        f.close()
        return render_to_response('timing/thanks.html', {'timelist':timelist})
    else:
        return redirect('/instructions/')


