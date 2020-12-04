from django.db import models
from bases.models import ClaseModelo
from inventario.models import Producto



class Proveedor(ClaseModelo):

    nombre = models.CharField(max_length=250,unique=True)
    apellido = models.CharField(max_length=250)
    dirección = models.CharField(max_length=250)
    teléfono = models.CharField(max_length=250)
    email = models.CharField(max_length=100,unique=True)

    def __str__(self):

        return '{}'.format(self.nombre)

    class Meta:
        verbose_name_plural = "Proveedores"


class ComprasEnc(ClaseModelo):

    fecha_compra = models.DateField(null=True,blank=True)
    fecha_factura = models.DateField()
    observacion = models.TextField(blank=True, null=True)
    numero_factura = models.CharField(max_length=100)
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)

    proveedor_form = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.observacion)

    def save(self):
        self.observacion = self.observacion.upper()
        self.total = self.sub_total - self.descuento
        super(ComprasEnc,self).save()

    class Meta:
        verbose_name_plural = 'Encabezado Compras'
        verbose_name = 'Encabezado Compra'

class ComprasDet(ClaseModelo):

    compra = models.ForeignKey(ComprasEnc, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.BigIntegerField(default=0)
    precio_prv = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)
    costo = models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)
