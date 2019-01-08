from django.forms import ModelForm
from pizzeriaApp.models import Client,Pizza
class clientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name','lastname','ci']

class pizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = ['size','price']
        

