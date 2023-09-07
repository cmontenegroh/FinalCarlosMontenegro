from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView

urlpatterns = [
path('register/', register, name='register'),
]