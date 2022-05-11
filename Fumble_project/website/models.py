from django.db import models
import datetime

# Create your models here.


class User(models.Model):
    isCapt = models.BooleanField(default=False)
    address = models.TextField(default="")
    password = models.TextField(default="")
    email = models.TextField(default="")
    is_active = models.BooleanField(default=True)
    last_login = models.TextField(default="")
    teams = models.TextField(default="")


class Team(models.Model):
    captain = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    teamName = models.TextField(default="")
    mmr = models.IntegerField()
    teamAddress = models.TextField(default="")
    sport = models.TextField(default="")


