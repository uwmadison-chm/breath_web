import sys
import csv

from django.core.management.base import NoArgsCommand

from timing import models


class Command(NoArgsCommand):
    help = "Print ID -> label mappings for demographic data"

    def handle_noargs(self, **options):
        writer = csv.writer(sys.stdout, delimiter=",")
        header_row = ['session_key', 'participant_num', 'viewed', 'timestamp']
        writer.writerow(header_row)

        for viewing in models.Viewing.objects.all():
            ppt_num = '0'
            if viewing.participant:
                ppt_num = viewing.participant.participant_number
            data = [
                viewing.session_key, ppt_num, viewing.view_key,
                viewing.created_at]
            writer.writerow(data)
