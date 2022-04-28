from django.http import HttpResponse
from django.shortcuts import render
import logging

logger = logging.getLogger()

def home(request):
    return render(request, 'website/home.html')


def about(request):
    return render(request, 'website/about.html')


def login(request):
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
