from django.db import models

class Login(models.Model):
    email = models.CharField(max_length=20)
    pptID = models.IntegerField()

class Participant(models.Model):
    pptID = models.IntegerField()

class Run(models.Model):
    ppt = models.ForeignKey(Participant)
    date = models.DateTimeField()
    
class Keypresses(models.Model):
    run = models.ForeignKey(Run)
    keypresses = models.TextField()
