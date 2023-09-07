

from django.shortcuts import render, redirect
from .models import Perfil
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def ver_perfil(request):
    perfil = Perfil.objects.get(usuario=request.user)
    return render(request, 'AppPerfil/ver_perfil.html', {'perfil': perfil})


def editar_perfil(request):
    perfil = Perfil.objects.get(usuario=request.user)
    if request.method == 'POST':
        perfil.nombre = request.POST['nombre']
        perfil.descripcion = request.POST['descripcion']
        perfil.email = request.POST['email']
        perfil.contraseña = request.POST['contraseña']
        if 'avatar' in request.FILES:
            perfil.avatar = request.FILES['avatar']
        perfil.save()
        messages.success(request, 'Perfil actualizado con éxito.')
        return redirect('ver_perfil')
    return render(request, 'AppPerfil/editar_perfil.html', {'perfil': perfil})


def borrar_perfil(request):
    perfil = Perfil.objects.get(usuario=request.user)
    if request.method == 'POST':
        perfil.delete()
        messages.success(request, 'Perfil borrado con éxito.')
        return redirect('logout')  # Redirigir a la página de inicio de sesión o a donde desees
    return render(request, 'AppPerfil/borrar_perfil.html')

