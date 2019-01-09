from pizzeriaApp.models import Pizza,Ingredient,Order,Pizza_Ingredient
from pizzeriaApp.models import Client
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.http import HttpResponse
from pizzeriaApp.forms import pizzaForm,ingredienteForm
from django.forms import modelformset_factory


def indexpizzas(request):
    pizzas = Pizza.objects.all()
    return render(request,'pizzas.html',{'pizzas': pizzas})

def createpizza(request):
    """PizzaFormSet = modelformset_factory(Pizza,fields =('size', 'ingredients'))"""
    if request.method == 'POST':
        form = pizzaForm(request.POST)
      
        """form = PizzaFormSet(request.POST)"""        
        form.price = 0
        if form.is_valid():
            print(form.cleaned_data['ingredients'])
            print("giiiiiiiiiiiiiiiiiiiiiiiiiiiii")
            print(form)
            precio = 0
            
            print(precio)
            order = Order.objects.last()
            form.price = precio
            form.fk_orden = order.id
          
            pizza =form.save(commit=False)
            pizza.fk_order = order
            
           
            pizza.save()
            for ingrediente in form.cleaned_data['ingredients']:
                precio = precio +ingrediente.price
                Pizza_Ingredient.objects.create(fk_pizza = pizza, fk_ingredient =ingrediente)
            pizza.price = precio + pizza.size.price
            print(pizza.ingredients.all())
            print(pizza.fk_order)
            print(pizza.fk_order.id)
            pizza.save()
            return redirect('mostrarpizza',id = pizza.id)
        else:
            print(form)
            field_errors = [ (field.label, field.errors) for field in form] 
            print(field_errors)
            print("invalido")    
    else:
        form = pizzaForm()
       
    return render(request,'pizzacreate.html',{'form':form})

def showpizza(request,id):
    pizza = Pizza.objects.get(id = id)
    return render(request,'showpizza.html',{'pizza': pizza})

def indexingredientes(request):
    ingredientes = Ingredient.objects.all()
    return render(request,'indexingrediente.html',{'ingredientes':ingredientes})


def showorden(request,id):
    orden = Order.objects.get(id = id)
    pizzas = orden.pizza_set.all()
    total = 0
    for pizza in pizzas:
        total = total +pizza.price
    orden.total = total
    orden.save()
    return render(request,'showorden.html',{'orden':orden,'pizzas':pizzas})