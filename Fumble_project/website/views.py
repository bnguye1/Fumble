from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def login(request):
    return render(request, 'website/login.html')

def register(request):
    return render(request, 'website/register.html')

def navbar(request):
    return render(request, 'website/navbar.html')
    
def profile(request):
    return render(request, 'website/profile.html')
    
def map(request):
    return render(request, 'website/map.html')
