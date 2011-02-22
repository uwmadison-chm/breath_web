import datetime
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
    
    @classmethod
    def first(klass):
        return klass.objects.all()[0]

    def __unicode__(self):
        return self.label

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
    email = models.CharField(max_length=255, unique=True, blank=False)

    participant_number = models.CharField(
        max_length=8, unique=True, default=_random_ppt_num)

    gender = models.ForeignKey(
        Gender, default=Gender.first, null=True)

    handedness = models.ForeignKey(
        Handedness, default=Handedness.first, null=True)

    race = models.ForeignKey(
        Race, default=Race.first, null=True)

    ethnicity = models.ForeignKey(
        Ethnicity, default=Ethnicity.first, null=True)

    country_of_residence = models.ForeignKey(
        CountryOfResidence, default=CountryOfResidence.first, null=True)

    education_level = models.ForeignKey(
        EducationLevel, default=EducationLevel.first, null=True)

    spirituality = models.ForeignKey(
        Spirituality, default=Spirituality.first, null=True)

    religious_affiliation = models.ForeignKey(
        ReligiousAffiliation, default=ReligiousAffiliation.first, 
        null=True)
    
    political_identity = models.ForeignKey(
        PoliticalIdentity, default=PoliticalIdentity.first, null=True)
    
    occupation = models.ForeignKey(
        Occupation, default=Occupation.first, null=True)
    
    postal_code = models.CharField(max_length=5, blank=True, null=True)

    birth_year = models.IntegerField(default=0)
    
    birth_month = models.IntegerField(default=0)
    
    consent_given = models.BooleanField(default=False)
    
    email_ok = models.BooleanField(default=False)
    
    @property
    def has_demographics(self):
        return self.birth_year is not None and self.birth_year > 0
    
    @property
    def started_runs(self):
        return self.run_set.filter(started_at__isnull=False)
    
    @property
    def next_run_number(self):
        return self.started_runs.count() + 1
    
    @property
    def has_run_data(self):
        return self.next_run_number > 1
    
    def __unicode__(self):
        return "Participant(email='%s', participant_number='%s')" % (
            self.email, self.participant_number
        )
    

class Run(StampedTrackedModel):
    participant = models.ForeignKey(Participant)

    planned_length_sec = models.IntegerField(default=60*15)

    # Informational only...
    run_num = models.IntegerField(default=0)
    
    started_at = models.DateTimeField(blank=True, null=True)

    finished_at = models.DateTimeField(blank=True, null=True)
    
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    
    def start(self):
        self.started_at = datetime.datetime.utcnow()
        self.run_num = self.participant.next_run_number
    
class Response(StampedTrackedModel):
    run = models.ForeignKey(Run)
    
    key = models.CharField(max_length=1)
    
    press_num = models.IntegerField()
    
    ms_since_run_start = models.IntegerField()
    
    timezone_offset_min = models.IntegerField(default=0)
    
    class Meta:
        unique_together = ("run", "press_num")


class Viewing(StampedTrackedModel):
    session_key = models.CharField(max_length=255, blank=True, null=True)

    participant = models.ForeignKey(Participant, blank=True, null=True)

    view_key = models.CharField(max_length=255)
    
    def __unicode__(self):
        return "Viewing(session_key='%s', participant=%s, view_key='%s')" %(
            self.session_key, self.participant, self.view_key
        )