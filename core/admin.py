from django.contrib import admin
from .models import Producto, Venta, Cliente, Suscrito, Usuario, Categoria
# Register your models here.
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Cliente)
admin.site.register(Suscrito)
admin.site.register(Usuario)
admin.site.register(Categoria)