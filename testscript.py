import sys, os, re

# Don't modify system path. Rely on the caller to correctly export PYTHONPATH

from django.core.management import setup_environ
from meditime import settings

setup_environ(settings)
from timing.models import Participant, Run, Keypresses

for keypress in Keypresses.objects.all():
    print str(keypress.run.date)
    timelist = re.findall(r'\r\n(\d* \d*)', keypress.keypresses)
    for timing in timelist:
        print str(keypress.run.ppt.pptID) + "  " + timing
    print "\n"

