from django.contrib import admin
from .models import Client, Order,Size,Ingredient,Pizza

admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Ingredient)
admin.site.register(Pizza)
admin.site.register(Size)
# Register your models here.
