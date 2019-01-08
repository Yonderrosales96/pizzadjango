from pizzeriaApp.models import Pizza
from django.shortcuts import render
from django.http import HttpResponseRedirect
def index(request):
    pizzas = Pizza.objects.all()
    return render(request,'pizzas.html',{'pizzas': pizzas})

"""def create(request):
    if request.method == 'POST':"""
        