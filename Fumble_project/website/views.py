from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.conf import settings
from .models import User, Team
from datetime import datetime
from django.contrib.gis.measure import D

import logging
import ast, json

from .models import User, Team

logger = logging.getLogger()

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')


def teams(request):
    if "user" in request.session and request.session['user'] != {}:
        if request.method == "POST":
            name = request.POST['name-field']
            email = request.POST['email-field']
            address = request.POST['address-field']
            sports = request.POST['sport-field']

            try:
                user = User.objects.get(email__exact=email)

                if user is not None:
                    # Convert sports to JSON list
                    sports_json = json.dumps(sports.split(','))
                    team = Team(teamName=name, captain=user, mmr=0, teamAddress=address, sport=sports_json)
                    team.save()

                    # Get the captain's team list
                    team_list = user.teams

                    # First time captain has a team
                    if team_list == "":
                        user.teams = str([name])

                    else:
                        # Convert list to string and then add new team into list
                        teams_list = ast.literal_eval(team_list)
                        teams_list.append(name)
                        user.teams = json.dumps(teams_list)

                    user.save()
                    messages.info(request, f"{name} has been registered as a team.")

                    return HttpResponseRedirect('/teams')

            except Exception:
                messages.error(request, "Please enter the correct email.")
                return HttpResponseRedirect('/teams')
        else:
            # Get a list of all the registered teams
            all_teams = Team.objects.all()

            if len(all_teams) != 0:
                context = {
                    'all_teams': all_teams,
                    'has_teams': True
                }

            else:
                context = {
                    'has_teams': False
                }

            return render(request, 'website/teams.html', context)
    else:
        return HttpResponseRedirect('/login')


def login_view(request):
    if request.method == "POST":
        email = request.POST['email-field']
        password = request.POST['password-field']
        user = User.objects.get(email__exact=email)

        if user is not None and user.password == password:
            user.last_login = datetime.now()
            user.save()
            request.session['user'] = user.id
            return HttpResponseRedirect('/home')

        else:
            messages.error(request, "Incorrect email address and/or password.")
            return HttpResponseRedirect('/login')

    return render(request, 'website/login.html')


def logout_view(request):
    if request.session:
        logout(request)
        return render(request, 'website/logout.html')
    else:
        return render(request, 'website/login.html')


def register(request):
    if request.method == 'POST':
        # TODO - Implement adding users to database when register
        password = request.POST["password"]
        email = request.POST["email"]
        user = User(isCapt=False, password=password, email=email)
        user.save()

        return HttpResponseRedirect("/login")

    else:
        return render(request, 'website/register.html')


def profile(request):
    # Allow user to view their profile
    if "user" in request.session and request.session['user'] != {}:
        user = User.objects.get(id=request.session['user'])
        teams_list = ast.literal_eval(user.teams)
        team_objects = []

        if len(teams_list) != 0:
            for name in teams_list:
                a_team = Team.objects.get(teamName=name)
                team_objects.append(a_team)

            context = {
                'has_teams': True,
                'user': user,
                'user_teams': team_objects
            }

        else:
            context = {
                'has_teams': False,
                'user': user,
            }

        return render(request, 'website/profile.html', context)

    else:
        return HttpResponseRedirect('/login')


def map(request):

    if "user" in request.session and request.session['user'] != {}:
        teams = Team.objects.all()  # gets all registered team objects from database table
        context = {
            'teams': teams,
            'has_teams': True
        }
        if request.method == "POST": #this takes the input fields from respective forms
            mileRadius = request.POST["distance"]
            addressCenter = request.POST["address"]
            games = request.POST["games"]#filters based off query and returns results
            qs = Team.objects.filter(point__distance_gte=(addressCenter, D(mi=mileRadius)), sport=games)
            return qs #this's the part where the query is output to a table
        return render(request, 'website/map.html', context)

    else:
        return HttpResponseRedirect('/login')



def challenge(request):
    return render(request, 'website/challenge.html')

