# Generated by Django 2.1.5 on 2019-01-09 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeriaApp', '0002_auto_20190109_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='ingredients',
            field=models.ManyToManyField(blank=True, through='pizzeriaApp.Pizza_Ingredient', to='pizzeriaApp.Ingredient'),
        ),
    ]
