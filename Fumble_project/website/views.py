import ast
import json
import logging
from datetime import datetime
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render

from .models import User, Team, Match

logger = logging.getLogger()


def home(request):
    if "user" in request.session and request.session['user'] != {}:
        if request.method == "POST":
            confirm = request.POST['confirm-box']
            host = request.POST['host-team-name']
            opponent = request.POST['opponent-team-name']
            sport = request.POST['match-sport']

            # Find the match
            host_team = Team.objects.get(teamName=host)
            opponent_team = Team.objects.get(teamName=opponent)

            match = Match.objects.get(host_team=host_team, opponent_team=opponent_team, match_sport=sport)

            if match.opponent_team.captain.id == request.session['user']:
                if confirm == 'accept':
                    match.opponent_accept = True

            elif match.host_team.captain.id == request.session['user']:
                if confirm == 'reject':
                    match.host_accept = False

            # Check if both teams have accepted
            if match.opponent_accept and match.host_accept:
                match.match_status = "In-progress"

            elif not match.opponent_accept and not match.host_accept:
                match.match_status = "Cancelled"

            # For future, check for win/loss conditions
            # Fair note, this is just a stand-in, we do not actually have an MMR system working.
            if match.host_win and not match.opponent_win:
                match.match_status = "Completed"
                match.host_team.mmr += 100

            elif not match.host_win and match.opponent_win:
                match.match_status = "Completed"
                match.opponent_team.mmr += 100

            else:
                match.match_status = "Forfeit"
                match.opponent_team.mmr = 0
                match.host_team.mmr = 0

            match.save()
            return HttpResponseRedirect('/home')

        else:
            user = User.objects.get(id=request.session['user'])
            matches_list = Match.objects.all()

            try:
                teams_list = ast.literal_eval(user.teams)
                my_match_objects = []
                my_progress_matches = []

                if len(matches_list) != 0:
                    for match in matches_list:
                        if match.host_team.teamName in teams_list or match.opponent_team.teamName in teams_list:
                            if match.match_status == "Pending":
                                my_match_objects.append(match)

                            elif match.match_status == "In-progress":
                                my_progress_matches.append(match)

                    context = {
                        'has_matches': True,
                        'has_progress': True,
                        'user': user,
                        'matches': my_match_objects,
                        'in_progress': my_progress_matches
                    }

                else:
                    context = {
                        'has_matches': False,
                        'has_progress': False,
                        'user': user,
                    }

                return render(request, 'website/home.html', context)
            except Exception:
                return render(request, 'website/home.html', {})
    else:
        return HttpResponseRedirect('/login')


def about(request):
    return render(request, 'website/about.html', {})




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

                        if not user.isCapt:
                            user.isCapt = True

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
        password = request.POST["password"]
        email = request.POST["email"]
        user = User(isCapt=False, address="", password=password, email=email)
        user.save()

        return HttpResponseRedirect("/login")

    else:
        return render(request, 'website/register.html')


def profile(request):
    # Allow user to view their profile
    if "user" in request.session and request.session['user'] != {}:
        user = User.objects.get(id=request.session['user'])

        try:
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

        except Exception:
            return render(request, 'website/profile.html', {})

    else:
        return HttpResponseRedirect('/login')


def map(request):
    if "user" in request.session and request.session['user'] != {}:
        return render(request, 'website/map.html', {})

    else:
        return HttpResponseRedirect('/login')


def challenge(request):
    if "user" in request.session and request.session['user'] != {}:
        if request.method == "POST":
            team1 = request.POST['team1-name-field']
            team2 = request.POST['team2-name-field']
            sport = request.POST['sports-field']
            match_time = request.POST['time-field']

            # Get both team objects
            team1_obj = Team.objects.get(teamName=team1)
            team2_obj = Team.objects.get(teamName=team2)

            # Create match
            match = Match(host_team=team1_obj, opponent_team=team2_obj,
                          match_sport=sport, match_time=match_time)
            match.save()

            messages.info(request, f"A match request to team {team2_obj.teamName} has been sent.")
            return HttpResponseRedirect('/challenge')
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

            return render(request, 'website/challenge.html', context)

    else:
        return HttpResponseRedirect('/login')

