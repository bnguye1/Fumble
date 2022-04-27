from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
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

        user = authenticate(request, email=email, password=password)

        # User has correct login information
        if user is not None:
            login(request, user)
            return render(request, "http://localhost:8000/home")

        return HttpResponse(email + " " + password)
    else:
        return render(request, 'website/login.html')

def register(request):
    if request.method == 'POST':
        # TODO - Implement adding users to database when register
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        return HttpResponse(username + " " + password + " " + email)
    else:
        return render(request, 'website/register.html')

def navbar(request):
    return render(request, 'website/navbar.html')
    
def profile(request):
    return render(request, 'website/profile.html')
    
def map(request):
    return render(request, 'website/map.html')
