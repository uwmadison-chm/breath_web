import sys, os, re
sys.path.append("/home/benedict/coding/research/test/trunk/")

from django.core.management import setup_environ
import settings

setup_environ(settings)
from timing.models import Participant, Run, Keypresses

for keypress in Keypresses.objects.all():
    print str(keypress.run.date)
    timelist = re.findall(r'\r\n(\d* \d*)', keypress.keypresses)
    for timing in timelist:
        print str(keypress.run.ppt.pptID) + "  " + timing
    print "\n"

