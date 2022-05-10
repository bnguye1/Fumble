from django.db import models
import datetime

# Create your models here.


class User(models.Model):
    isCapt = models.BooleanField(default=False)
    address = models.TextField(default="")
    teamName = models.TextField(default="")
    password = models.TextField(default="")
    email = models.TextField(default="")
    is_active = models.BooleanField(default=True)
    last_login = models.TextField(default="")


# Currently WIP
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(default="", max_length=100)
    team_name = models.CharField(default="", max_length=100)
    last_login = models.CharField(default="", max_length=100)
    address = models.CharField(default="", max_length=100)


class Team(models.Model):
    captain = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    mmr = models.IntegerField()
    teamAddress = models.TextField(default="")
    sport = models.TextField()


