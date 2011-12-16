import datetime
import time
import random

from django.db import models
from django.conf import settings


class StampedTrackedModel(models.Model):
    """
    Abstract base class -- automatically records created_at, updated_at,
    and SCM revision of the code used to create the record.

    All models should inherit from this unless there's a good reason.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    scm_revision = models.CharField(
        "Code revision",
        max_length=255,
        default=settings.REPOSITORY_URL,
        editable=False)

    class Meta:
        abstract = True


def random_slug(slug_len):
    # Limit the the choices to characters that look dissimilar-ish.
    # Still lots of 'em.
    letters = 'bcdfghjkmnpqrstvz'

    def fx():
        charnums = range(slug_len)
        slug = ''.join([random.choice(letters) for cn in range(slug_len)])
        return slug
    return fx


class Experiment(StampedTrackedModel):
    """
    All the parameters associated with an experiment will live in here.
    Additionally, this contains a URL slug that'll be used to direct ppts
    to an individual experiment.
    """

    url_slug = models.SlugField(
        "URL slug",
        max_length=10,
        unique=True,
        default=random_slug(5))

    run_length_seconds = models.IntegerField(
        "Run length",
        help_text = "(Seconds)",
        default=60*15)

    survey_url = models.URLField(
        max_length=255)

    chime_on_error = models.BooleanField(
        default=False)

    run_instructions = models.TextField(
        blank=True,
        default="")

    guide_sound_file = models.FileField(
        blank=True,
        null=True,
        upload_to="guides")

    breath_time_key = models.CharField(
        max_length=1,
        default="J")

    end_cycle_key = models.CharField(
        max_length=1,
        default="K")

    cycle_length = models.IntegerField(
        default=9)

    practice_cycles = models.FloatField(
        default=1.5)

    last_exported_at = models.DateTimeField(
        auto_now_add=True)

    data_last_added_at = models.DateTimeField(
        auto_now_add=True)

    use_swf_url = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default=None)

    def __unicode__(self):
        return "%s: %s, created %s" % (
            self.pk, self.url_slug, self.created_at)

    @property
    def experiment_number(self):
        return self.pk

    @property
    def chime_on_error_js(self):
        if self.chime_on_error:
            return "true"
        else:
            return "false"

    @property
    def has_guide_sound_js(self):
        if self.guide_sound_file is not None and self.guide_sound_file <> '':
            return "true"
        return "false"

    @property
    def run_length_minutes(self):
        return self.run_length_seconds/60

    @property
    def breath_time_keycode(self):
        return ord(self.breath_time_key)

    @property
    def end_cycle_keycode(self):
        return ord(self.end_cycle_key)

    @property
    def needs_export(self):
        export = False
        if (self.data_last_added_at > self.last_exported_at):
            export = True
        return export

    def save(self, *args, **kwargs):
        self.breath_time_key = self.breath_time_key.upper()
        self.end_cycle_key = self.end_cycle_key.upper()
        super(Experiment, self).save(*args, **kwargs)


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
    def email_ok_num(self):
        if self.email_ok:
            return 1
        return 0

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
            self.email, self.participant_number)


class Run(StampedTrackedModel):

    experiment = models.ForeignKey(Experiment)

    participant = models.ForeignKey(Participant)

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

    duration_ms = models.IntegerField(default=0)

    timezone_offset_min = models.IntegerField(default=0)

    played_error_chime = models.BooleanField(default=False)

    class Meta:
        unique_together = ("run", "press_num")

    @property
    def participant_number(self):
        return self.run.participant.participant_number

    @property
    def experiment_number(self):
        return self.run.experiment.pk

    @property
    def run_number(self):
        return self.run.run_num

    @property
    def run_finished(self):
        finished = 0
        if self.run.finished_at is not None:
            finished = 1
        return finished

    @property
    def keypress_number(self):
        return self.press_num + 1

    @property
    def keycode(self):
        return ord(self.key)

    @property
    def server_timestamp_sec(self):
        return time.mktime(self.created_at.timetuple())

    @property
    def timezone_offset_sec(self):
        return self.timezone_offset_min*60

    @property
    def played_chime(self):
        bool_to_int = {True: 1, False: 0}
        return bool_to_int[self.played_error_chime]

    def __update_experiment_time(self):
        self.run.experiment.data_last_added_at = self.created_at
        self.run.experiment.save()

    def save(self, *args, **kwargs):
        super(Response, self).save(*args, **kwargs)
        self.__update_experiment_time()


class Viewing(StampedTrackedModel):
    session_key = models.CharField(max_length=255, blank=True, null=True)

    participant = models.ForeignKey(Participant, blank=True, null=True)

    view_key = models.CharField(max_length=255)

    def __unicode__(self):
        return "Viewing(session_key='%s', participant=%s, view_key='%s')" %(
            self.session_key, self.participant, self.view_key)
