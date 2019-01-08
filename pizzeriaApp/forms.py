from django.forms import ModelForm
from pizzeriaApp.models import Client
class clientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name','lastname','ci']