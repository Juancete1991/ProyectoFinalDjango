from django.contrib import admin

# Register your models here.
from .models import Gasto

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'monto', 'fecha', 'categoria')
    list_filter = ('categoria', 'fecha')
    search_fields = ('descripcion', 'nota')