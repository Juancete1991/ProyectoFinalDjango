from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Gasto(models.Model):
    CATEGORIAS = [
        ('AL', 'Alimentación'),
        ('TR', 'Transporte'),
        ('ED', 'Educación'),
        ('OC', 'Ocio'),
        ('OT', 'Otros'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gastos')
    descripcion = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    categoria = models.CharField(max_length=2, choices=CATEGORIAS, default='OT')
    nota = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-fecha', '-id']

    def __str__(self):
        return f"{self.descripcion} - ${self.monto} ({self.get_categoria_display()})"
