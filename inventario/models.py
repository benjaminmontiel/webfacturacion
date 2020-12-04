from django.db import models
from bases.models import ClaseModelo

class Categoria(ClaseModelo):


# Variable de clase "Descripcion" define atributos y métodos compartidos
# por todas las instancias de la clase Categoria.

    Descripcion = models.CharField(
            max_length=100,
            help_text='Descripcion de la categoria',
            unique=True
    )


#  Definición de métodos de instancia como __str__() y save() hacen referencia al
# comportamiento que tendrá una instancia específica de la clase, cuando se inicie
# el objeto.


    def __str__(self):
        return '{}'.format(self.Descripcion)

    def save(self):
        self.Descripcion = self.Descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = 'Categorias'


class Sub_Categoria(ClaseModelo):

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
            max_length=100,
            help_text='Descripcion de la categoria',
            unique=True
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.Descripcion, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Sub_Categoria,self).save()


    class Meta:
        verbose_name_plural = 'Sub Categorias'
        unique_together = ('categoria','descripcion')



class Marca(ClaseModelo):

    descripcion = models.CharField(
            max_length=100,
            help_text='Descripcion de la Marca',
            unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()

    class Meta:
        verbose_name_plural = 'Marcas'


class UnidadMedida(ClaseModelo):

    descripcion = models.CharField(
            max_length=100,
            help_text='Descripcion de la UM',
            unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)


    def save(self):
        self.descripcion = self.descripcion.upper()
        super(UnidadMedida,self).save()

    class Meta:
        verbose_name_plural = 'Unidades de Medida'

class Producto(ClaseModelo):

    codigo = models.CharField(max_length=20, unique=True)

    codigo_de_barra = models.CharField(max_length=50)
    descripcion = models.CharField (max_length=100)
    precio = models.FloatField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)


    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    sub_categoria = models.ForeignKey(Sub_Categoria, on_delete=models.CASCADE)
    unidad_medida= models.ForeignKey(UnidadMedida, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto,self).save()

    class Meta:
        verbose_name_plural = "Productos"
        unique_together = ('codigo','codigo_de_barra')
