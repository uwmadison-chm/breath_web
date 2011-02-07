import sys, os, re

# Will have to modify the system path if you are testing locally
# For example, here is what I add:
sys.path.append("/home/benedict/coding/research/test/trunk/")
#sys.path.append("/var/www/lib/python2.5/site-packages/")
#sys.path.append("/var/www/apps/")

from django.core.management import setup_environ
#import meditime.settings
import settings

setup_environ(settings)
from timing.models import Participant, Run, Keypresses

for keypress in Keypresses.objects.all():
    print str(keypress.run.date)
    timelist = re.findall(r'\r\n(\d* \d*)', keypress.keypresses)
    for timing in timelist:
        print str(keypress.run.ppt.pptID) + "  " + timing
    print "\n"

