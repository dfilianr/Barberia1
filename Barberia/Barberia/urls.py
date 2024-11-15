"""
URL configuration for Barberia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from Barberia import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.views import indexTemplateView
from core.registro.views import registroView
from core.login.views import inicioSesionUsuario,LogoutView
from core.agenda.views import AgendaListiView,AgendaCreateView,actualizarAgenda,eliminarAgenda

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',indexTemplateView.as_view(),name=''),
    path('iniSesion/',inicioSesionUsuario.as_view(),name='iniSesion'),
    path('regisUsua/',registroView.as_view(),name='regisUsua'),
    path('logout/',LogoutView.as_view(next_page=''),name='logout'),

    path('listaagenda',AgendaListiView.as_view(),name='listaagenda'),
    path('crearagenda/',AgendaCreateView.as_view(),name='crearagenda'),
    path('actualizaragenda/<int:pk>', actualizarAgenda.as_view(),name='actualizaragenda'),
    path('eliminaragenda/<int:pk>', eliminarAgenda.as_view(),name='eliminaragenda'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
