from typing import Any
from django.db import models
from costumer_products.models import Products

# Create your models here.
class detalle_venta(models.Model):

    producto = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True )
    cantidad =models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
   
    def __init__(self, producto , cantidad , monto) -> None:
        self._producto = producto
        self._cantidad = cantidad
        self._monto = monto
        


    def calcula_tot(self):
        pass
