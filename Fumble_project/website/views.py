from django.http import HttpResponse
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
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def login(request):

    if request.method == "POST":
        try:
            email = request.POST['email-field']
            password = request.POST['password-field']
            user = User.objects.get(email__exact=email)

            # A "completely" safe approach
            if user:
                if user.password == password:
                    messages.info(request, "You have logged in successfully!")
                    return HttpResponseRedirect('/home')
            else:
                messages.error(request, "Incorrect email address and/or password.")
                return HttpResponseRedirect('/login')

        except Exception:
            messages.error(request, "Incorrect email address and/or password.")
            return HttpResponseRedirect('/login')

    return render(request, 'website/login.html')

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
