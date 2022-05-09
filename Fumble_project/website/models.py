from django.db import models


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
"""
class UserProfile(models.Model):
    template_name = '/profile.html'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField("", blank=True)
"""


class Team(models.Model):
    captain = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    mmr = models.IntegerField()
    teamAddress = models.TextField(default="")
    sport = models.TextField()


