# Generated by Django 2.1.5 on 2019-01-09 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeriaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]