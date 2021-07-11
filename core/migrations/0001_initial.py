# Generated by Django 3.2.3 on 2021-07-10 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='Identificador del Producto')),
                ('nombreProducto', models.CharField(max_length=70, verbose_name='Nombre Producto')),
                ('descProducto', models.CharField(max_length=70, verbose_name='Descripción Producto')),
                ('cantStock', models.CharField(max_length=50, verbose_name='Stock disponible')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('idVenta', models.IntegerField(primary_key=True, serialize=False, verbose_name='Identificador de la Venta')),
                ('nroVenta', models.CharField(max_length=20, verbose_name='Número de Venta')),
                ('cantidad', models.CharField(max_length=20, verbose_name='Cantidad')),
                ('montoVenta', models.CharField(max_length=50, verbose_name='Monto Total a Pagar')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
    ]