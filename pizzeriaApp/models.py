from django.db import models

# Create your models here.
class Client (models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    ci = models.IntegerField()

class Order (models.Model):
    fk_client = models.ForeignKey(Client,on_delete=models.CASCADE)
    buy_date = models.DateTimeField('fecha de compra')
    total = models.DecimalField(max_digits=15,decimal_places=10)

class Size (models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #TYPE_OF_SIZE = ('Pequeña','Mediana','Grande')
    # name = models.CharField(max_length=20,choices = TYPE_OF_SIZE)

class Ingredient (models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)


class Pizza (models.Model):
    fk_order = models.ForeignKey(Order,on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(
        Ingredient,
        through='Pizza_Ingredient',
        through_fields=('fk_pizza','fk_ingredient'),
    )
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)

class Pizza_Ingredient (models.Model):
    fk_pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    fk_ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE)
