from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import Categoria, Sub_Categoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, Sub_CategoriaForm, MarcaForm, UnidadMedidaForm, ProductoForm
from django.contrib.messages.views import SuccessMessageMixin




class CategoriaView(LoginRequiredMixin, PermissionRequiredMixin,generic.ListView):

    model = Categoria
    template_name = 'base/inventario/categoria.html'
    context_object_name='obj'
    login_url= 'bases:login'
    
    # para que se pueda tener acceso a esta vista, el cliente debe tener el permiso
    # especificado en la variable permission_required
    permission_required="inventario.view_categoria"


class CategoriaNew(SuccessMessageMixin,LoginRequiredMixin,\
        generic.CreateView):

    model = Categoria
    template_name = 'base/inventario/categoriaform.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url =  reverse_lazy('inventario:categoria')
    login_url = 'bases:login'
    success_message = 'Categoria Creada Satisfactoriamente'


    # método de instancia, se aplica solo a un objeto específico (self)
    def form_valid(self,form):


        # la función pasa dos variables, una del lado del request y otra del response.
        # una es 'self' que hace referencia/apunta al objeto que
        # almacena la información de la request POST solicitada, pasada a la vista
        # y que queremos validar.

        # y otra que contiene la data del modelform con el que trabajamos y pasamos
        # al usuari.



        # cómo el campo de usuario no está habilitado en el formulario, y por ende
        # no sabemos a qué usuario atribuir los datos posteados, debemos especificar
        # que antes de guardar el formulario, asociemos que quien envió el POST es
        # el user loggeado/ autenticado y dentro de la sesión.

        form.instance.Usuario = self.request.user
        # acá antes de guardar el formulario estamos reemplazando el valor de la variable
        # Usuario por el valor de user que viene de la request.

        return super().form_valid(form)


class CategoriaEdit(SuccessMessageMixin,LoginRequiredMixin, generic.UpdateView):

    model = Categoria
    template_name = 'base/inventario/categoriaform.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url =  reverse_lazy('inventario:categoria')
    login_url = 'bases:login'
    success_message = 'Categoria Actualizada Satisfactoriamente'

    def form_valid(self, form):

        form.instance.Usuario_mod  = self.request.user.id
        return super().form_valid(form)

class CategoriaDel(LoginRequiredMixin, generic.DeleteView):

    model = Categoria
    template_name = 'base/inventario/categoria_del.html'
    context_object_name = 'obj'
    success_url =  reverse_lazy('inventario:categoria')



class SubCategoriaView(LoginRequiredMixin,PermissionRequiredMixin,generic.ListView):


    model = Sub_Categoria
    template_name = 'base/inventario/subcategoria.html'
    context_object_name='obj'
    login_url= 'bases:login'
    permission_required = 'inventario.view_subcategoria'


class SubCategoriaNew(LoginRequiredMixin, generic.CreateView):

    model = Sub_Categoria
    template_name = 'base/inventario/subcategoriaform.html'
    context_object_name = 'obj'
    form_class = Sub_CategoriaForm
    success_url =  reverse_lazy('inventario:sub_categoria')
    login_url = 'bases:login'


    def form_valid(self,form):

        form.instance.Usuario  = self.request.user

        return super().form_valid(form)


class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):


    model = Sub_Categoria
    template_name = 'base/inventario/subcategoriaform.html'
    context_object_name = 'obj'
    form_class = Sub_CategoriaForm
    success_url =  reverse_lazy('inventario:sub_categoria')
    login_url = 'bases:login'

    def form_valid(self, form):

        form.instance.Usuario_mod  = self.request.user.id
        return super().form_valid(form)



class SubCategoriaDel(LoginRequiredMixin, generic.DeleteView):

    model = Sub_Categoria
    template_name = 'base/inventario/subcategoria_del.html'
    context_object_name = 'obj'
    success_url =  reverse_lazy('inventario:sub_categoria')


class MarcaView(LoginRequiredMixin, generic.ListView):

    model = Marca
    template_name = 'base/inventario/marcalist.html'
    context_object_name = 'obj'
    login_url= 'bases:login'


class MarcaNew(LoginRequiredMixin, generic.CreateView):

    model = Marca
    template_name = 'base/inventario/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url =  reverse_lazy('inventario:marca')
    login_url = 'bases:login'

    def form_valid(self,form):

        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse

        form.instance.Usuario = self.request.user
        return super().form_valid(form)


class MarcaEdit(LoginRequiredMixin, generic.UpdateView):

    model = Marca
    template_name = 'base/inventario/marca_form.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inventario:marca')
    login_url = 'bases:login'
    form_class = MarcaForm

    def form_valid(self, form):

        form.instance.Usuario_mod  = self.request.user.id
        return super().form_valid(form)


def marca_inactivar(request, pk):

    marca = Marca.objects.filter(pk=pk).first()
    contexto = {}
    template_name ='base/inventario/marca_inactivar.html'

    if not marca:
        return redirect('inventario_marca')

    if request.method == "GET":

        contexto = {'obj': marca}


        return render(request,template_name,contexto)

    if request.method == "POST":

        marca.Estado = False
        marca.save()

        return redirect('inventario:marca')

class MarcaView(LoginRequiredMixin, generic.ListView):

    model = Marca
    template_name = 'base/inventario/marcalist.html'
    context_object_name = 'obj'
    login_url= 'bases:login'


class UnidadMedidaView(LoginRequiredMixin, generic.ListView):

    model = UnidadMedida
    template_name = 'base/inventario/um_list.html'
    context_object_name = 'obj'
    login_url= 'bases:login'


class UnidadMedidaNew(LoginRequiredMixin, generic.CreateView):

    model = UnidadMedida
    template_name = 'base/inventario/um_form.html'
    context_object_name = 'obj'
    login_url= 'bases:login'
    success_url=reverse_lazy('inventario:um')
    form_class = UnidadMedidaForm

    def form_valid(self, form):

        form.instance.Usuario  = self.request.user
        return super().form_valid(form)




class UnidadMedidaEdit(LoginRequiredMixin, generic.UpdateView):

    model = UnidadMedida
    template_name = 'base/inventario/um_form.html'
    context_object_name = 'obj'
    login_url= 'bases:login'
    success_url=reverse_lazy('inventario:um')
    form_class = UnidadMedidaForm

    def form_valid(self, form):

        form.instance.Usuario_mod  = self.request.user.id
        return super().form_valid(form)


def unidad_medida(request,pk):

    um = UnidadMedida.objects.filter(pk=pk).first()


    if request.method == 'GET':

        contexto = {'obj': um}

        return render(request,'base/inventario/um_inactivar.html',contexto)

    if request.method == 'POST':

        um.Estado = False
        um.save()

        return redirect('inventario:um')


class ProductoView(LoginRequiredMixin,generic.ListView):

    model = Producto
    template_name = 'base/inventario/producto_list.html'
    context_object_name='obj'
    login_url= 'bases:login'


class ProductoNew(LoginRequiredMixin, generic.CreateView):

    model = Producto
    template_name = 'base/inventario/producto_form.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
    success_url = reverse_lazy('inventario:producto_list')
    form_class = ProductoForm



    def form_valid(self, form):


        form.instance.Usuario  = self.request.user
        return super().form_valid(form)

class ProductoEdit(LoginRequiredMixin, generic.UpdateView):

    model = Producto
    template_name = 'base/inventario/producto_form.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
    success_url = reverse_lazy('inventario:producto_list')
    form_class = ProductoForm


    def form_valid(self, form):


        form.instance.Usuario_mod  = self.request.user.id

        return super().form_valid(form)



# en esta función pasamos dos parámetros. Una es la variables request,
# que contiene la información con la solicitud HTTP que ha hecho el usuario a través del
# navegador, y por otro lado, pasamos también el id del recurso que se solicita, y que el cliente
# quiere modificar.

# Debemos especificarle a la función que producto específico queremos inactivar.
# por eso le pasamos el pk o id del objeto.


def producto_inactivar(request, pk):

    producto = Producto.objects.filter(pk=pk).first()
    contexto = {}
    template_name ='base/inventario/producto_inactivar.html'

    if not producto:
        return redirect('inventario:producto_list')

    if request.method == "GET":

        contexto = {'obj': producto}


        return render(request,template_name,contexto)

    if request.method == "POST":

        producto.Estado = False
        producto.save()

        return redirect('inventario:producto_list')
