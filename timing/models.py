import random

from django.db import models
from django.conf import settings


"""
Abstract base class -- automatically records created_at, updated_at,
and SCM revision of the code used to create the record.

All models should inherit from this unless there's a good reason.
"""

class StampedTrackedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    scm_revision = models.CharField(
        "Code revision", 
        max_length=255, 
        default=settings.REPOSITORY_URL,
        editable=False)
    
    class Meta:
        abstract = True


class Demographic(StampedTrackedModel):
    label = models.CharField(max_length=255, default='', unique=True)
    position = models.IntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ['position']

class Gender(Demographic):
    pass

class Handedness(Demographic):
    pass

class Race(Demographic):
    pass

class Ethnicity(Demographic):
    pass

class CountryOfResidence(Demographic):
    pass

class EducationLevel(Demographic):
    pass

class Spirituality(Demographic):
    pass

class ReligiousAffiliation(Demographic):
    pass

class PoliticalIdentity(Demographic):
    pass

class Occupation(Demographic):
    pass

def _random_ppt_num():
    return str(random.randint(100000, 999999))

class Participant(StampedTrackedModel):
    email = models.CharField(max_length=255, unique=True)

    participant_number = models.CharField(
        max_length=8, unique=True, default=_random_ppt_num)

    gender = models.ForeignKey(
        Gender, blank=True, null=True, default=None)

    race = models.ForeignKey(
        Race, blank=True, null=True, default=None)

    ethnicity = models.ForeignKey(
        Ethnicity, blank=True, null=True, default=None)

    country_of_residence = models.ForeignKey(
        CountryOfResidence, blank=True, null=True, default=None)

    education_level = models.ForeignKey(
        EducationLevel, blank=True, null=True, default=None)

    spirituality = models.ForeignKey(
        Spirituality, blank=True, null=True, default=None)

    religious_affiliation = models.ForeignKey(
        ReligiousAffiliation, blank=True, null=True, default=None)
    
    policital_identity = models.ForeignKey(
        PoliticalIdentity, blank=True, null=True, default=None)
    
    occupation = models.ForeignKey(
        Occupation, blank=True, null=True, default=None)
    
    postal_code = models.CharField(max_length=5, blank=True, null=True)

    birth_year = models.IntegerField(default=0)
    
    birth_month = models.IntegerField(default=0)
    
    consent_given = models.BooleanField(default=False)
    
    email_ok = models.BooleanField(default=False)
    
    @property
    def has_demographics(self):
        return self.birth_year is not None and self.birth_year > 0
    

class Run(StampedTrackedModel):
    participant = models.ForeignKey(Participant)
    planned_length_sec = models.IntegerField(default=60*15)
    started_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    
class Response(StampedTrackedModel):
    run = models.ForeignKey(Run)
    key = models.CharField(max_length=1)
    press_num = models.IntegerField()
    ms_since_run_start = models.IntegerField()
    
    class Meta:
        unique_together = ("run", "press_num")


