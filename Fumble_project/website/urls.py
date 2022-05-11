from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='website-home'),
    path('about/', views.about, name='website-about'),
    path('login/', views.login_view, name='website-login'),
    path('register/', views.register, name='website-register'),
    path('profile/', views.profile, name='website-profile'),
    path('map/', views.map, name='website-map'),
    path('teams/', views.teams, name='website-teams'),
    path('logout/', views.logout_view, name='website-logout'),
]
