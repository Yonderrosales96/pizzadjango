from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('cliente',views.create,name = 'crearcliente'),
    path('<int:id>/cliente',views.show,name = 'mostrarcliente')
]
