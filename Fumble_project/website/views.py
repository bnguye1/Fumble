from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import redirect
from django.conf import settings
import logging


logger = logging.getLogger()

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                message.info(request, 'You have successfully logged in!')
                return render(request, "website/home.html")

            else:
                messages.info(request, 'Invalid E-mail Address or Password.')
                return HttpResponse(password + " " + email)

        except Exception as ex:
            return redirect('/')
    else:
        return render(request, "website/login.html")


def register(request):
    if request.method == 'POST':
        # TODO - Implement adding users to database when register
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        # These coordinates are from a random McDonald's somewhere in the world
        user = User(isCapt=False, locationX=37.033289, locationY=-95.619456, teamName="", password=password, email=email)
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
