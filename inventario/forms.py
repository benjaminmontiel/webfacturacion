from django.forms import ModelForm
from django import forms
from .models import Categoria, Sub_Categoria, Marca, UnidadMedida, Producto


class CategoriaForm(forms.ModelForm):

    class Meta:

        model = Categoria

        fields = ['Descripcion','Estado']

        labels = {'Descripcion': "Descripcion de la Categoria",
                 'Estado': "Estado de la Categoría"}

        widget = {'Descripcion': forms.TextInput }

        def __init__(self,*args,**kwargs):

            super().__init__(*args,**kwargs)
            for field in iter(self.fields):
                self.field[field].widget.attrs.update({'class':'form-control'})


class Sub_CategoriaForm(forms.ModelForm):

    categoria = forms.ModelChoiceField(queryset=Categoria.objects.filter(
    Estado=True).order_by('Descripcion'))



    class Meta:

            model = Sub_Categoria

            fields = ['categoria','descripcion','Estado']

            labels = {'descripcion': "Descripcion de la Sub Categoria",
                    'Estado': "Estado de la Sub Categoría"}

            widget = {'descripcion': forms.TextInput }

            def __init__(self,*args,**kwargs):

                super().__init__(*args,**kwargs)
                for field in iter(self.fields):
                    self.field[field].widget.attrs.update({'class':'form-control'})

                self.fields['categoria'].empty_label = "Seleccione Categoria"


class MarcaForm(forms.ModelForm):

    class Meta:

            model = Marca

            fields = ['descripcion','Estado']

            labels = {'descripcion': "Descripcion de la Marca",
                    'Estado': "Estado de la Marca"}

            widget = {'descripcion':forms.TextInput}


            def __init__(self,*args,**kwargs):

                super().__init__(*args,**kwargs)
                for field in iter(self.fields):
                    self.field[field].widget.attrs.update({'class':'form-control'})

class UnidadMedidaForm(forms.ModelForm):

    class Meta:

            model = UnidadMedida

            fields = ['descripcion','Estado']

            labels = {'descripcion': "Descripcion de la Marca",
                    'Estado': "Estado de la Marca"}

            widget = {'descripcion':forms.TextInput}


            def __init__(self,*args,**kwargs):

                super().__init__(*args,**kwargs)
                for field in iter(self.fields):
                    self.field[field].widget.attrs.update({'class':'form-control'})

class ProductoForm(forms.ModelForm):

        # instancia ModelForm vinculada a objeto modelo tendrá un atributo
        # "instance" que permitirá acceder a la instancia específica del modelo.


    class Meta:


            model = Producto


            fields = ['codigo','codigo_de_barra','descripcion', 'precio',
                     'marca', 'sub_categoria', 'Estado']


            def __init__(self,*args,**kwargs):

                super().__init__(*args,**kwargs)
                for field in iter(self.fields):
                    self.field[field].widget.attrs.update({'class':'form-control'})
