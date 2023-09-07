from django.urls import path
from .views import *
from .models import Mensaje
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView



urlpatterns = [
    
   
    
    path('lista_mensajes/', login_required(ListView.as_view(model=Mensaje, template_name='AppMensajes/mensaje_list.html')), name='lista_mensajes'),
    path('enviar_mensaje/', login_required(CreateView.as_view(model=Mensaje, template_name='AppMensajes/mensaje_form.html', fields=['receptor', 'contenido'])), name='enviar_mensaje'),
    
]