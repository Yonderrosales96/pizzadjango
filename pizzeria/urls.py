"""pizzeria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import include
from pizzeriaApp.views import viewventas


def hello_world(request):
    return HttpResponse('Hello world')


urlpatterns = [
    path('admin/pizzeriaApp/generalVentas',viewventas.getVentas),
    path('admin/pizzeriaApp/VentasDiaria',viewventas.getVentasDiaria),
    path('admin/pizzeriaApp/search',viewventas.search),
    path('admin/pizzeriaApp/VentasBySize',viewventas.getVentasBySize),
    path('admin/pizzeriaApp/VentasByCliente',viewventas.getVentasByCliente),
    path('admin/pizzeriaApp/VentasByIngrediente',viewventas.getVentasByIngrediente),
    path('admin/', admin.site.urls),
    path('hello-world/',hello_world),
    path('pizzeriaApp/', include('pizzeriaApp.urls')),
]
