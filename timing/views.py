from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from models import Login, Participant, Run, Keypresses
import re, datetime, random

import csv
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def base(request):
    return redirect('/apps/meditime/login')

def login(request):
    if request.method == 'POST':        
        if "email" in request.session:
            return redirect('/apps/meditime/instructions')
        else:
            if "email" in request.POST:
                email = request.POST['email']
                idSet = Login.objects.filter(email__iexact=email)
                pptID = 0

                if idSet.count() == 0:
                    rand = random.randint(100000, 999999)
                    while Login.objects.filter(pptID=rand).count() > 0:
                        rand = random.randint(100000, 999999)
                    pptID = rand
                    Login.objects.create(email=email, pptID=rand)
                    Participant.objects.create(pptID=rand)
                else:
                    pptID = idSet[0].pptID

                request.session['id'] = pptID
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
        sessID = request.session['id']
        pressTimings = request.POST['timing']

        participant = Participant.objects.get(pptID=sessID)
        newRun = Run(ppt=participant, date=datetime.datetime.now())
        newRun.save()
        newKeypresses = Keypresses(run=newRun, keypresses=pressTimings)
        newKeypresses.save()
        #newrun = Run(user=username, date=datetime.datetime.now(), keypresses=timing)
        #newrun.save()
        
        return render_to_response('timing/thanks.html')
    else:
        return redirect('/apps/meditime/login/')


