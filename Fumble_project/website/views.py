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
    if "email" in request.session:
        email = request.session['email']
        param = {'email': logged_in}
        return render(request, 'website/home.html', param)

    else:
        return render(request, 'website/login.html', {})


def about(request):
    if "email" in request.session:
        email = request.session['email']
        param = {'email': logged_in}
        return render(request, 'website/about.html', param)

    else:
        return render(request, 'website/about.html', {})


def login_view(request):
    if request.method == "POST":
        email = request.POST['email-field']
        password = request.POST['password-field']
        user = User.objects.get(email__exact=email)

        if user and user.password == password:
            login(request, user)
            return render(request, 'website/home.html', {'email': email})

        else:
            messages.error(request, "Incorrect email address and/or password.")
            return HttpResponseRedirect('/login')

    return render(request, 'website/login.html', {})


def logout(request):
    if "email" in request.session:
        try:
            del request.session['session']
            return HttpResponseRedirect('/login')

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


def profile(request):
    if "email" in request.session:
        email = request.session['email']
        param = {'email': email}
        return render(request, 'website/profile.html', param)

    else:
        return render(request, 'website/login.html', {})


def map(request):
    if "email" in request.session:
        email = request.session['email']
        param = {'email': email}
        return render(request, 'website/map.html', param)

    else:
        return render(request, 'website/login.html', {})