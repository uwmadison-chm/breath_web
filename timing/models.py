from django.db import models

class Login(models.Model):
    email = models.CharField(max_length=20)
    idNum = models.IntegerField()

class Participant(models.Model):
    idNum = models.IntegerField()

class Run(models.Model):
    ptcp = models.ForeignKey(Participant)
    date = models.DateTimeField()
    
class Keypresses(models.Model):
    run = models.ForeignKey(Run)
    keypresses = models.TextField()


'''
class Run(models.Model):
    user = models.CharField(max_length=30)
    date = models.DateTimeField('Date of run')
    keypresses = models.CharField(max_length=6000)
    def __unicode__(self):
        return self.user + "@" + str(self.date)
'''
