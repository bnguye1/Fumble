from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='website-home'),
    path('about/', views.about, name='website-about'),
    path('navbar/', views.navbar, name='navigation-bar'),
    path('profile/', views.profile, name='website-profile'),
    path('map/', views.map, name='website-map'),
]
