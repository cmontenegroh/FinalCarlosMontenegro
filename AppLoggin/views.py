from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm




def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request,"AppBlog/inicio.html", {"mensaje":f"Bienvenido, {usu}"})
            else:
                return render(request,"AppLoggin/login.html", {"form":form, "mensaje":"Datos erroneos"})
                
        else:
            return render(request,"AppLoggin/login.html", {"form":form, "mensaje":"Datos erroneos"})
    else:
        form=AuthenticationForm()
        return render(request,"AppLoggin/login.html", {"form":form})
