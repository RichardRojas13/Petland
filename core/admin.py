from django.contrib import admin
from .models import Producto, Venta, Cliente

# Register your models here.
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Cliente)