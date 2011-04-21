import sys
import csv

from django.core.management.base import NoArgsCommand

from timing import models

class Command(NoArgsCommand):
    help = "Print demographic data as CSV"
    
    def handle_noargs(self, **options):
        ppts = models.Participant.objects.all().order_by('pk')
        
        field_names = ['participant_number', 'email', 'email_ok_num']
        writer = csv.writer(sys.stdout, delimiter=",")
        writer.writerow(field_names)
        for ppt in ppts:
            writer.writerow([
                getattr(ppt, field) for field in field_names
            ])