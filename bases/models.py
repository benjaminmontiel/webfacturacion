from django.db import models

from django.contrib.auth.models import User

class ClaseModelo(models.Model):

    Estado = models.BooleanField(default=True)
    Fecha_creacion = models.DateTimeField(auto_now_add=True)
    Fecha_modificacion = models.DateTimeField(auto_now=True)
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Usuario_mod = models.IntegerField(blank=True, null=True)


    class Meta:
        abstract=True
