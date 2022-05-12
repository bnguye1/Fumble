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


# Experimental Model for Challenge System
class Match(models.Model):
    host_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="host_team", default=0)
    opponent_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="opponent_team", default=0)
    host_win = models.BooleanField(default=False)
    opponent_win = models.BooleanField(default=False)
    host_accept = models.BooleanField(default=False)
    opponent_accept = models.BooleanField(default=False)
    match_sport = models.TextField(default="")
    match_time = models.TextField(default="")
    match_status = models.TextField(default="Waiting for both teams to accept")



