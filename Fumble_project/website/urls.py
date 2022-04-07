from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='website-home'),
    path('about/', views.about, name='website-about'),
    path('register/', views.register, name='website-register')
]