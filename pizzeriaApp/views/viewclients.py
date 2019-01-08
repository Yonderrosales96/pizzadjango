from pizzeriaApp.models import Pizza,Order
from pizzeriaApp.models import Client
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.http import HttpResponse
from pizzeriaApp.forms import clientForm
import datetime

def create(request):
    if request.method == 'POST':
        form = clientForm(request.POST)
        if form.is_valid():
            now = datetime.datetime.now()
            orden = Order(buy_date = now,total = 0)
            client =form.save()
            orden.fk_client = client
            orden.save()
            # return redirect('mostrarcliente',id = client.id)
            #return HttpResponseRedirect('createpizza',"Text only, please.", content_type="text/plain")
            return redirect ('createpizza')
    else:
        form = clientForm()
    return render(request,'clientecreate.html',{'form':form})

def show(request,id):
    cliente = Client.objects.get(id = id)
    return render(request,'showcliente.html',{'cliente': cliente})


def index(request):
    clientes = Client.objects.all()
    return render(request,'indexcliente.html',{'clientes': clientes})
