from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.conf import settings
from .models import User
import logging

logger = logging.getLogger()


def home(request):
    if request.session.has_key('email'):
        email = request.session['email']
        return render(request, 'website/home.html', {'email': email})
    else:
        return HttpResponseRedirect('/login')

def about(request):
    return render(request, 'website/about.html')


def login_view(request):
    if request.method == "POST":
        email = request.POST['email-field']
        password = request.POST['password-field']
        user = User.objects.get(email__exact=email)

        if user and user.password == password:
            login(request, user)
            return render(request, 'website/navbar.html', {'email': user.email})
        else:
            messages.error(request, "Incorrect email address and/or password.")
            return HttpResponseRedirect('/login')

    return render(request, 'website/login.html')

def logout(request):
    try:
        del request.session['email']
    except Exception:
        pass

    return HttpResponseRedirect('/login')

def register(request):
    if request.method == 'POST':
        # TODO - Implement adding users to database when register
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        user = User(isCapt=False, teamName="", address="", password=password, email=email)
        user.save()

        return HttpResponse(username + " " + password + " " + email)

    else:
        return render(request, 'website/register.html')


def navbar(request):
    return render(request, 'website/navbar.html')


def profile(request):
    return render(request, 'website/profile.html')


def map(request):
    return render(request, 'website/map.html')
