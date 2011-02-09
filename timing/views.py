from django.shortcuts import render_to_response, redirect
from models import Participant, Run
import re, datetime, random

import csv
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

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
    return render_to_response('run_task.html')

def thanks(request):
    return render_to_response('thanks.html')


