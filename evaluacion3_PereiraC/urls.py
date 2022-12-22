"""evaluacion3_PereiraC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('listaPersonas/', views.listaPersonas),
    path('agregarpersona/', views.agregarpersona),
    path('eliminar/<int:id>', views.eliminarPersona),
    path('actualizar/<int:id>', views.actualizaPersona),
    path('inscritos/', views.inscritos),
    path('intitutos/', views.intitutosLista, name='instituto'),
    path('detalleIntitutos/<int:pk>', views.intitutosDetalle, name='instituto'),
    path('personasInscritas/', views.personasInscritas.as_view(), name='personas'),
    path('personasDetalles/<int:pk>', views.personasDetalles.as_view(), name='personas'),
    
]
