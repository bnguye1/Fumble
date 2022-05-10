from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.conf import settings
from .models import User
from .models import Profile
import logging

logger = logging.getLogger()


def home(request):
    return render(request, 'website/home.html')



def about(request):
    return render(request, 'website/about.html')


def login_view(request):
    if request.method == "POST":
        email = request.POST['email-field']
        password = request.POST['password-field']
        user = User.objects.get(email__exact=email)

        if user is not None and user.password == password:
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
        user = User(isCapt=False, teamName="", address="", password=password, email=email)
        user.save()
        u_profile = Profile(user, user.email)
        u_profile.save()

        return HttpResponseRedirect("/login")

    else:
        return render(request, 'website/register.html')


def profile(request):
    # Allow user to view their profile
    if "user" in request.session and request.session['user'] != {}:
        user = User.objects.get(id=request.session['user'])
        context = {
            'user': user
        }
        return render(request, 'website/profile.html', context)

    else:
        return HttpResponseRedirect('/login')


def map(request):
    if "user" in request.session and request.session['user'] != {}:
        return render(request, 'website/map.html')

    else:
        return HttpResponseRedirect('/login')

