from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import Proveedor
from .forms import ProveedorForm
from django.http import HttpResponse
from inventario.models import Producto



class ProveedorView(LoginRequiredMixin,generic.ListView):

    model = Proveedor
    template_name = 'base/compras/proveedores_list.html'
    context_object_name = 'obj'
    login_url= 'bases:login'

class ProveedorNew(LoginRequiredMixin, generic.CreateView):

    model = Proveedor
    template_name = 'base/compras/proveedor_form.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
    success_url = reverse_lazy('compras:proveedores_list')
    form_class = ProveedorForm


    def form_valid(self,form):

        form.instance.Usuario = self.request.user
        return super().form_valid(form)


class ProveedorEdit(LoginRequiredMixin, generic.UpdateView):

    model = Proveedor
    template_name = 'base/compras/proveedor_form.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
    success_url = reverse_lazy('compras:proveedores_list')
    form_class = ProveedorForm

    def form_valid(self,form):


        form.instance.Usuario_mod = self.request.user.id

        return super().form_valid(form)

def proveedores_inactivar(request,pk):

    proveedor = Proveedor.objects.filter(pk=pk).first()

    if not proveedor:

            return HttpResponse('Proveedor no existe' + str(pk))

    if request.method == 'GET':

        contexto = {'obj': proveedor}

        template_name = 'base/compras/proveedor_inactivar.html'

        return render(request,template_name, contexto)


    if request.method == 'POST':

        proveedor.Estado = False
        proveedor.save()

        return redirect('compras:proveedores_list')
