from django.db import models


# Create your models here.


class User(models.Model):
    isCapt = models.BooleanField(default=False)
    locationX = models.FloatField(default=0)
    locationY = models.FloatField(default=0)
    teamName = models.TextField(default="")
    password = models.TextField(default="")
    email = models.TextField(default="")


class Team(models.Model):
    captain = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    mmr = models.IntegerField()
    teamHouseX = models.FloatField()
    teamHouseY = models.FloatField()
    sport = models.TextField()
