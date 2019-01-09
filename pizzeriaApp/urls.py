from django.urls import path
from . import views
from django.shortcuts import render
def welcome(request):
    return render(request,'welcome.html')


urlpatterns = [
    path('', views.index, name='index'),
    path('cliente',views.create,name = 'crearcliente'),
    path('<int:id>/cliente',views.show,name = 'mostrarcliente'),
    path('cliente/index',views.index,name= 'indexcliente'),
    path('pizza',views.createpizza, name = 'createpizza'),
    path('<int:id>/pizza',views.showpizza,name = 'mostrarpizza'),
    path('ingredientes',views.indexingredientes, name = 'indexingredientes'),
    path('orden/<int:id>/',views.showorden,name = "showorden"),
    path('welcome',welcome)

]
