from typing import Any
from django.db import models
from costumer_categoria.models import Categoria



class User(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    dni = models.CharField(max_length=10)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    fecha_alta = models.DateField(auto_now_add=True)
    estado = models.IntegerField(default=1)

    def __init__(self, nombre, apellido, email , password , dni , idcategoria):
        self.nombre =  nombre
        self.apellido =  apellido
        self.email =  email
        self.password =  password
        self.dni =  dni
        categoria = idcategoria


    def __str__(self):
        return f' Id : {self.id}  Nombre :  {self.nombre}  Apellido : {self.apellido}  E-mail: {self.email}'

class UserStandar(User):
    def __init__(self, nombre, apellido, email , password , dni , idcategoria): 
        super().__init__(nombre, apellido, email , password , dni, idcategoria)


class UserAdmin(User):
    def __init__(self, nombre, apellido, email , password , dni,idcategoria):
        super().__init__(nombre, apellido, email , password , dni, idcategoria)






