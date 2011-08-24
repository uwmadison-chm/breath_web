import os

from django.core.management.base import NoArgsCommand

import timing
from timing import models


class Command(NoArgsCommand):
    help = "Load demographic text files into database"

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

    def handle_noargs(self, **options):
        fixture_dir = os.path.join(
            os.path.dirname(timing.__file__), "fixtures")

        for klass in self.__class__.demographic_classes:
            fixture_file = os.path.join(
                fixture_dir, klass.__name__.lower()+".txt")
            print(fixture_file)
            with open(fixture_file, 'r') as f:
                for num, label in enumerate(f):
                    l = label.strip()
                    try:
                        inst = klass(label=l, position=num)
                        inst.save()
                    except:
                        print("Didn't add %s to %s" % (l, klass))
