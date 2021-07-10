from django.db import models

# Create your models here.


#Productos
class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="Identificador del Producto")
    nombreProducto = models.CharField(max_length=70, verbose_name="Nombre Producto", help_text="Introduzca su nombre")
    cantStock = models.IntegerField(verbose_name="Stock disponible", help_text="Introduzca cantidad de Stock disponible")

    def __str__(self):
        return self.nombreProducto

# Modelo para las Ventas
class Venta(models.Model):
    nroVenta = models.IntegerField(primary_key=True, verbose_name="Identificador de la Venta")
    idProducto = models.ForeignKey(Producto, on_delete=models.SET('ProductoEliminado'), help_text="Selecciona Producto")
    cantidad = models.CharField(max_length=20, null=True, blank=True, verbose_name="Modelo", help_text="Introduzca el modelo")
    montoVenta = models.IntegerField(verbose_name="Monto Total a pagar")

    def __str__(self):
        return self.nroVenta

