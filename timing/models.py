from django.db import models

class Run(models.Model):
    user = models.CharField(max_length=30)
    date = models.DateTimeField('Date of run')
    keypresses = models.CharField(max_length=6000)
    def __unicode__(self):
        return self.user + "@" + str(self.date)
