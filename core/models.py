from django.db import models

# Create your models here.


#Productos
class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="Identificador del Producto")
    nombreProducto = models.CharField(max_length=70, verbose_name="Nombre Producto")
    descProducto = models.CharField(max_length=70, verbose_name="Descripción Producto")
    cantStock = models.CharField(max_length=50,verbose_name="Stock disponible")

    def __str__(self):
        return self.nombreProducto

# Modelo para las Ventas
class Venta(models.Model):
    idVenta  = models.IntegerField(primary_key=True, verbose_name="Identificador de la Venta")
    nroVenta = models.CharField(max_length=20, verbose_name="Número de Venta")
    cantidad = models.CharField(max_length=20, verbose_name="Cantidad")
    montoVenta = models.CharField(max_length=50,verbose_name="Monto Total a Pagar")
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nroVenta
