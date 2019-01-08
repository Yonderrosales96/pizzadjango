from pizzeriaApp.models import Pizza
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.http import HttpResponse
from pizzeriaApp.forms import clientForm
def index(request):
    return HttpResponse("metodo index")

def create(request):
    if request.method == 'POST':
        form = clientForm(request.POST)
        if form.is_valid():
            client =form.save() 
            return redirect('mostrarcliente',id = client.id)
    else:
        form = clientForm()
    return render(request,'clientecreate.html',{'form':form})      

def show(request,id):
    return HttpResponse("el id cliente es ${0}" .format(id) )
    