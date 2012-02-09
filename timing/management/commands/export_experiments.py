import sys
import csv

from django.core.management.base import NoArgsCommand

from timing import models


class Command(NoArgsCommand):
    help = "Print experiment parameters as CSV"

    def handle_noargs(self, **options):
        exps = models.Experiment.objects.all().order_by('pk')

        field_names = [
            'experiment_number', 'url_slug', 'run_length_seconds',
            'survey_url', 'chime_on_error', 'run_instructions',
            'guide_sound_file', 'breath_time_key', 'breath_time_keycode',
            'end_cycle_key', 'end_cycle_keycode', 'cycle_length',
            'practice_cycles']
        writer = csv.writer(sys.stdout, delimiter=",")
        writer.writerow(field_names)
        for exp in exps:
            data = [getattr(exp, field) for field in field_names]
            data = [unicode(d).encode('utf-8') for d in data]
            writer.writerow(data)
