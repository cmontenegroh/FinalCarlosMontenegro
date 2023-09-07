from django.shortcuts import render
from django.http import HttpResponse
from .forms import  RegistroUsuarioForm

def register(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre_usuario=info["username"]
            form.save()
            return render(request, "AppRegistro/inicio.html", {"mensaje":f"Triper {nombre_usuario} creado exitosamente"})
        else:
            return render(request, "AppRegistro/register.html", {"form":form, "mensaje":"Datos erroneos"})
    else:
        form=RegistroUsuarioForm()
        return render(request, "AppRegistro/register.html", {"form":form})
