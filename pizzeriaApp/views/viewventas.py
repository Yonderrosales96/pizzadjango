from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from pizzeriaApp.models import Order,Ingredient,Size,Client
from django.http import HttpResponse
import json

def getVentas (request):
    orders = Order.objects.all()
    return render(request,'generalVentas.html',{'orders': orders})

def getVentasDiaria (request):
    return render(request,'VentaDiaria.html')

def getVentasByIngrediente (request):
    ingredients = Ingredient.objects.all()
    return render(request,'ventasByIngrediente.html',{'ingredients':ingredients})

def getVentasBySize (request):
    sizes = Size.objects.all()
    return render(request,'ventasBySize.html',{'sizes':sizes})

def getVentasByCliente (request):
    clients = Client.objects.all()
    return render(request,'ventasByCliente.html',{'clients':clients})

def search (request):
    date = request.GET.get('date') #dicionario
    ingredient = request.GET.get('ingredient')
    size = request.GET.get('size')
    client = request.GET.get('client')
    if (bool(date)):
        orders = Order.objects.filter(buy_date__date = date)
    elif( bool(ingredient)):
        orders = Order.objects.filter(pizza__ingredients__id = ingredient)
    elif( bool(size)):
        orders = Order.objects.filter(pizza__size__id = size)
    elif( bool(client)):
        orders = Order.objects.filter(fk_client = client).order_by('total')

    orders = [order_serializer(order) for order in orders]
    return HttpResponse (json.dumps(orders),content_type="application/json")

def order_serializer (order):
    return {'id':order.id,'buy_date':order.buy_date.strftime('%m/%d/%Y'),'total':str(order.total)}

# a[0].pizza_set.all()
# b[0].size
# c=b[0].ingredients.all()



# getVentas = staff_member_required(getVentas)
