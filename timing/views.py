from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from models import Run
import re, datetime

import csv
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def base(request):
    return redirect('/apps/meditime/login')

def login(request):
    if request.method == 'POST':        
        if "id" in request.session:
            return redirect('/apps/meditime/instructions')
        else:
            if "id" in request.POST:
                request.session['id'] = request.POST['id']
                return redirect('/apps/meditime/instructions')
            else:
                return redirect('/apps/meditime/login')
    else:
        return render_to_response('timing/login.html')

def instructions(request):
    if "id" in request.session:
        return render_to_response('timing/instructions.html')
    else: 
        return redirect('/apps/meditime/login/')

def practice(request):
    if "id" in request.session:
        return render_to_response('timing/practice.html')
    else:
        return redirect('/apps/meditime/login/')

def run(request):
    if "id" in request.session:
        return render_to_response('timing/timing.html')
    else:
        return redirect('/apps/meditime/login/')

def submit(request):
    if request.method == 'POST':
        username = request.session['id']
        timing = request.POST['timing']

        timelist = re.findall(r'\d+', timing)
        newrun = Run(user=username, date=datetime.datetime.now(), keypresses=timing)
        newrun.save()
        
        #saveloc = '/home/benedict/coding/research/meditime/output/' + username + str(datetime.datetime.now())
        #f = open(saveloc, 'w')
        #f.write(timing)
        #f.close()
        return render_to_response('timing/thanks.html', {'timelist':timelist})
    else:
        return redirect('/apps/meditime/login/')


