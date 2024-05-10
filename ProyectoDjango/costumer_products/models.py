from django.db import models
from categoria_producto.models import CategoriaProducto


class Products(models.Model):
    nombre = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.SET_NULL, null=True )
   

    def __str__(self):
        return f' Id : {self.id}  nombre :  {self.nombre}  cantidad : {self.cantidad}  precio: {self.precio}'