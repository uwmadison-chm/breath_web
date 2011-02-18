import sys
import time
import csv

from django.core.management.base import NoArgsCommand

from timing import models

class Command(NoArgsCommand):
    help = "Print response data as CSV"
    
    def handle_noargs(self, **options):
        writer = csv.writer(sys.stdout, delimiter=",")
        # We're going to write:
        # participant #, run #, run_finished, press #, key_code, time_ms, server_time
        runs = models.Run.objects.all()
        header = [
            'participant_number',
            'run_number',
            'run_finished',
            'keypress_number',
            'keycode',
            'ms_since_run_start',
            'server_timestamp_sec',
            'timezone_offset_sec'
        ]
        writer.writerow(header)
        for run in runs:
            run_finished = 0
            if run.finished_at is not None:
                run_finished = 1
            for resp in run.response_set.order_by('press_num'):
                keycode = ord(resp.key)
                data = [
                    run.participant.participant_number,
                    run.run_num,
                    run_finished,
                    resp.press_num+1,
                    keycode,
                    resp.ms_since_run_start,
                    time.mktime(resp.created_at.timetuple()),
                    resp.timezone_offset_min*60
                ]
                writer.writerow(data)