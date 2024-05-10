from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f'Cateogoria {self.categoria
        }'
