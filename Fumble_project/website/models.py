from django.db import models


# Create your models here.
class User(models.Model):
    isCapt = models.BooleanField()
    locationX = models.FloatField()
    locationY = models.FloatField()
    teamName = models.TextField()
    password = models.TextField()
    email = models.TextField()


class Team(models.Model):
    captain = models.ForeignKey(User, on_delete=models.CASCADE)
    mmr = models.IntegerField()
    teamHouseX = models.FloatField()
    teamHouseY = models.FloatField()
    sport = models.TextField()
