# Generated by Django 5.0.4 on 2024-05-10 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria_producto', '0001_initial'),
        ('costumer_products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categoria_producto.categoriaproducto'),
        ),
    ]
