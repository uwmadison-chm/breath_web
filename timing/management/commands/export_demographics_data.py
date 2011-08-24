import sys
import csv

from django.core.management.base import NoArgsCommand

from timing import models


class Command(NoArgsCommand):
    help = "Print demographic data as CSV"

    def handle_noargs(self, **options):

        field_names = [
             'participant_number'
            ,'gender_id'
            ,'handedness_id'
            ,'race_id'
            ,'ethnicity_id'
            ,'country_of_residence_id'
            ,'education_level_id'
            ,'spirituality_id'
            ,'religious_affiliation_id'
            ,'political_identity_id'
            ,'occupation_id'
            ,'birth_year'
            ,'birth_month']

        writer = csv.writer(sys.stdout, delimiter=",")
        writer.writerow(field_names)
        for ppt in models.Participant.objects.all():
            writer.writerow([
                getattr(ppt, field) for field in field_names])
