from django.forms import ModelForm
from django import forms
from .models import Proveedor


class ProveedorForm(forms.ModelForm):

    class Meta:

        model = Proveedor

        fields = ['nombre','apellido','dirección','teléfono','email','Estado']
