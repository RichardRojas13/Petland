from django.db import models

# Create your models here.


#CATEGORIA

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id Categoria")
    nombreCategoria = models.CharField(max_length=50, verbose_name="Nombre Categoria")

    def _str_(self):
        return self.nombreCategoria