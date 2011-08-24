import sys
import csv

from django.core.management.base import NoArgsCommand

from timing import models


class Command(NoArgsCommand):
    help = "Print ID -> label mappings for demographic data"

    def handle_noargs(self, **options):
        writer = csv.writer(sys.stdout, delimiter=",")
        header_row = ['Field', 'id', 'label']
        writer.writerow(header_row)

        demographic_classes = [
             models.Handedness
            ,models.Spirituality
            ,models.Gender
            ,models.Race
            ,models.Occupation
            ,models.Ethnicity
            ,models.ReligiousAffiliation
            ,models.PoliticalIdentity
            ,models.CountryOfResidence
            ,models.EducationLevel]

        for klass in demographic_classes:
            results = klass.objects.all()
            for row in results:
                writer.writerow([
                    klass.__name__,
                    row.pk,
                    row.label])
