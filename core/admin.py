from django.contrib import admin
from .models import Producto, Venta, Cliente, Usuario, Suscrito

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Suscrito)