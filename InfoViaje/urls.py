from django.contrib import admin
from django.urls import path, include
from AppBlog.views import inicio, aeropuertos, trips
from AppMensajes.views import lista_mensajes, enviar_mensaje
from AppLoggin.views import login_request
from AppRegistro.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('AppBlog/', include('AppBlog.urls')),
    path('AppLoggin/', include('AppLoggin.urls')),
    path('AppMensajes/', include('AppMensajes.urls')),
    path('AppRegistro/', include('AppRegistro.urls')),
    path('AppPerfil/', include('AppPerfil.urls'))#si hubiera otra app, incluiria el path aqui
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
