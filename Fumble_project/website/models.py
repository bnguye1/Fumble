from django.db import models

# Create your models here.
class User(models.Model):
    isCapt = models.BooleanField()
    locationX = models.FloatField()
    locationY = models.FloatField()
    teamName = models.TextField()


class Team(models.Model):
    captain = models.ForeignKey(User)
    mmr = models.IntegerField()
    teamHouseX = models.FloatField()
    teamHouseY = models.FloatField()
    sport = models.TextField()

