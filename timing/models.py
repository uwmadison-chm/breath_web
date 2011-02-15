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


def _random_ppt_num():
    return str(random.randint(100000, 999999))

class Participant(StampedTrackedModel):
    email = models.CharField(max_length=255, unique=True)
    participant_number = models.CharField(
        max_length=8, unique=True, default=_random_ppt_num)


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
