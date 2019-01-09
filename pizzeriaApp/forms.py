from django.forms import ModelForm,ModelChoiceField
from pizzeriaApp.models import Client,Pizza,Ingredient

from django import forms

class clientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name','lastname','ci']

class pizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['size','ingredients']
        widgets = {
            'ingredients': forms.CheckboxSelectMultiple()
        }
    def __init__(self, *args, **kwargs):
        super(pizzaForm, self).__init__(*args, **kwargs)
        self.fields['size'].label = "Tamaño"
        self.fields['ingredients'].label = "Agrega los ingredientes"

class ingredienteForm(ModelForm):
    class Meta:
        model = Ingredient
        exclude = ()
    def __init__(self,*args,**kwargs):
        super(ingredienteForm, self).__init__(*args,**kwargs)
        self.fields['ingredientes'] = ModelChoiceField(queryset = Ingredient.objects.all(),empty_label= "Escoge un ingrediente")

def form_valid(self, form):
    """
    If the form is valid, redirect to the supplied URL
    """
    model_instance = form.save(commit=False)
    model_instance.post = self.object
    model_instance.author = self.request.user
    model_instance.pub_date = datetime.now()
    model_instance.publish = True
    model_instance.save()
    return HttpResponseRedirect(self.get_success_url())
