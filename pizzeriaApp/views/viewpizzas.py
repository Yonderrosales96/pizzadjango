from pizzeriaApp.models import Pizza
from pizzeriaApp.models import Client
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.http import HttpResponse
from pizzeriaApp.forms import pizzaForm
def indexpizzas(request):
    pizzas = Pizza.objects.all()
    return render(request,'pizzas.html',{'pizzas': pizzas})

def createpizza(request):
    if request.method == 'POST':
        form = pizzaForm(request.POST)
        if form.is_valid():
            pizza =form.save() 
            return redirect('mostrarpizza',id = client.id)
    else:
        form = pizzaForm()
    return render(request,'pizzacreate.html',{'form':form})      

def showpizza(request,id):
    pizza = Pizza.objects.get(id = id)
    return render(request,'showpizza.html',{'pizza': pizza})
