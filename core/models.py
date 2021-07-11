from django.db import models

# Create your models here.


#M para Productos
class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="Identificador del Producto")
    nombreProducto = models.CharField(max_length=70, verbose_name="Nombre Producto")
    descProducto = models.CharField(max_length=70, verbose_name="Descripción Producto")
    cantStock = models.CharField(max_length=50,verbose_name="Stock disponible")

    def __str__(self):
        return self.nombreProducto

# M para las Ventas
class Venta(models.Model):
    idVenta  = models.IntegerField(primary_key=True, verbose_name="Identificador de la Venta")
    nroVenta = models.CharField(max_length=20, verbose_name="Número de Venta")
    cantidad = models.CharField(max_length=20, verbose_name="Cantidad")
    montoVenta = models.CharField(max_length=50,verbose_name="Monto Total a Pagar")
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nroVenta

# M para Clientes
class Cliente(models.Model):
    idRutCli = models.IntegerField(primary_key=True, verbose_name="Número Rut del cliente")
    dvRun = models.CharField(max_length=1, verbose_name="Dígito Verificador")
    nombreCli = models.CharField(max_length=70, verbose_name="Nombre Cliente")
    apellidocli = models.CharField(max_length=80, verbose_name="Apellido Cliente")

    def __str__(self):
        return self.idRutCli

# M para Usuarios que Donan o se hayan Suscrito
class Suscrito(models.Model):
    idSuscripcion = models.AutoField(primary_key=True, verbose_name="Identificador de la Suscripción")
    nombreUser = models.CharField(unique=True, max_length=30, verbose_name="Nombre de usuario", help_text="Introduzca el nombre de usuario")
    fechaSuscripcion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha en la que el usuario se suscribió")

    def __str__(self):
        return self.idSuscripcion

# M para Clientes Registrados
class Usuario(models.Model):
    idUser = models.AutoField(primary_key=True, verbose_name="Identificador del Usuario")
    nombreUser = models.CharField(unique=True, max_length=30, verbose_name="Nombre de usuario", help_text="Introduzca el nombre de usuario")
    passwordUser = models.CharField(max_length=10, verbose_name="Contraseña", help_text="Introduzca la contraseña")
    idRutCli = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Número Rut sin dígito verificador")

    def __str__(self):
        return self.nombreUser    


