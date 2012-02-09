import sys
import datetime
import csv
import os
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError

from timing import models


class Command(BaseCommand):
    help = "Write a CSV file containing response data for each experiment"

    option_list = BaseCommand.option_list + (
        make_option('-f', '--force', help='Export all data, not just changed',
        action='store_true', dest='force', default=False), )

    def handle(self, *args, **kwargs):
        if not len(args) == 1:
            raise CommandError("Must specify output directory")
        out_dir = args[0]

        experiments = models.Experiment.objects.all()
        for exp in experiments:
            if kwargs['force'] or exp.needs_export:
                self._write_experiment_data(out_dir, exp)
                exp.last_exported_at = datetime.datetime.now()
                exp.save()

    def _write_experiment_data(self, path, exp):
        header = [
            'participant_number',
            'experiment_number',
            'run_number',
            'run_finished',
            'keypress_number',
            'keycode',
            'prompt_type',
            'ms_since_run_start',
            'duration_ms',
            'server_timestamp_sec',
            'timezone_offset_sec',
            'played_chime']

        out_file = "%s-%s-responses.csv" % (exp.pk, exp.url_slug)
        full_path = os.path.join(path, out_file)
        with open(full_path, 'w') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(header)
            for run in exp.run_set.all():
                responses = run.response_set.order_by('press_num')
                for resp in responses:
                    row = [getattr(resp, att) for att in header]
                    row = [unicode(d).encode('utf-8') for d in row]

                    writer.writerow(row)
