from django.shortcuts import render, redirect
from .models import  Mensaje
from django.http import HttpResponse
from .forms import  MensajeForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            receptor_id = form.cleaned_data['receptor']
            contenido = form.cleaned_data['contenido']
            try:
                receptor = User.objects.get(id=receptor_id)
                mensaje = Mensaje(emisor=request.user,
                                  receptor=receptor, contenido=contenido)
                mensaje.save()
                return redirect('lista_mensajes')
            except User.DoesNotExist:
                form.add_error('receptor', 'El receptor no existe.')

    else:
        form = MensajeForm()

    return render(request, 'AppMensajes/mensaje_form.html', {'form': form})



