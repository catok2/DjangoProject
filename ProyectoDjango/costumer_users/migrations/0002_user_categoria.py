# Generated by Django 5.0.4 on 2024-05-10 17:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costumer_categoria', '0001_initial'),
        ('costumer_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costumer_categoria.categoria'),
        ),
    ]
