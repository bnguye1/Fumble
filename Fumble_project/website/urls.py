from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='website-home'),
    path('about/', views.about, name='website-about'),
    path('login/', views.login, name='website-login')
    path('register/', views.register, name='website-register')
]