from django.shortcuts import render
from .models import  Aeropuerto, Trip
from django.http import HttpResponse
from .forms import  AeropuertoForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required




def inicio(request):
    return render(request,"AppBlog/inicio.html")

@login_required
def aeropuertos(request):
    if request.method=="POST":
        form=AeropuertoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            ciudad=info["ciudad"]
            comentario=info["comentario"]
            triper=info["triper"]
            fecha=info["fecha"]
            foto=fot0[foto]
            aeropuerto=Aeropuerto(nombre=nombre, ciudad=ciudad, comentario=comentario, triper=triper, fecha=fecha, foto=foto)
            
            aeropuerto.save()
            mensaje="Agregaste un aeropuerto"
           
           
        else:
            mensaje="Datos invalidos"
        aeropuertos=Aeropuerto.objects.all()   
        formulario_aeropuerto=AeropuertoForm()
        return render(request,"AppBlog/aeropuertos.html", {"mensaje":mensaje, "formulario":formulario_aeropuerto,"aeropuertos":aeropuertos})
    else:
        formulario_aeropuerto=AeropuertoForm()
        aeropuertos=Aeropuerto.objects.all()
            
       
    return render(request,"AppBlog/aeropuertos.html", {"formulario":formulario_aeropuerto, "aeropuertos": aeropuertos})
@login_required
def editarAeropuerto(request, id):
    aeropuerto = Aeropuerto.objects.get(id=id)
    if request.method == "POST":
        form = AeropuertoForm(request.POST, request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            aeropuerto.nombre = info["nombre"]
            aeropuerto.ciudad = info["ciudad"]
            aeropuerto.comentario = info["comentario"]
            aeropuerto.triper = info["triper"]
            aeropuerto.fecha = info["fecha"]
            if 'foto' in request.FILES:
                aeropuerto.foto = request.FILES['foto']

            aeropuerto.save()
            mensaje = "Aeropuerto editado correctamente"
            aeropuertos = Aeropuerto.objects.all()
            formulario_aeropuerto = AeropuertoForm()
            return render(request, "AppBlog/aeropuertos.html", {"mensaje": mensaje, "formulario": formulario_aeropuerto, "aeropuertos": aeropuertos})
        else:

            formulario_aeropuerto = AeropuertoForm(initial={"nombre": aeropuerto.nombre, "ciudad": aeropuerto.ciudad,
                                                   "comentario": aeropuerto.comentario, "triper": aeropuerto.triper, "fecha": aeropuerto.fecha, "foto": aeropuerto.foto})
            return render(request, "AppBlog/editarAeropuerto.html", {"formulario": formulario_aeropuerto, "aeropuerto": aeropuerto})
    else:

        formulario_aeropuerto = AeropuertoForm(initial={"nombre": aeropuerto.nombre, "ciudad": aeropuerto.ciudad,
                                               "comentario": aeropuerto.comentario, "triper": aeropuerto.triper, "fecha": aeropuerto.fecha, "foto": aeropuerto.foto})
        return render(request, "AppBlog/editarAeropuerto.html", {"formulario": formulario_aeropuerto, "aeropuerto": aeropuerto})


@login_required
def eliminarAeropuerto(request, id):
    aeropuerto=Aeropuerto.objects.get(id=id)
    aeropuerto.delete()
    aeropuertos=Aeropuerto.objects.all()   
    formulario_aeropuerto=AeropuertoForm()
    mensaje= "Aeropuerto eliminado"
    return render(request,"AppBlog/aeropuertos.html", {"mensaje":mensaje, "formulario":formulario_aeropuerto,"aeropuertos":aeropuertos})



@login_required
def trips(request):
    return render(request, "AppBlog/trips.html")

class TripList(LoginRequiredMixin, ListView):
    model= Trip
    template_name= "AppBlog/trips.html"
    
class TripCreacion(LoginRequiredMixin, CreateView):
    model= Trip
    success_url= reverse_lazy("trip_list")
    fields=['itinerario', 'empresa', 'comentario', 'triper', 'fecha']
    
class TripDetalle(LoginRequiredMixin, DetailView):
    model= Trip
    template_name= "AppBlog/trip_detalle.html"
    
class TripDelete(LoginRequiredMixin, DeleteView):
    model= Trip
    success_url= reverse_lazy("trip_list")
    
class TripUpdate(LoginRequiredMixin, UpdateView):
    model= Trip
    success_url= reverse_lazy("trip_list")
    fields=['itinerario', 'empresa', 'comentario', 'triper', 'fecha']