from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required



urlpatterns = [
    

    
    #Login, Logout y Register
    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]