from django.urls import path
from.views import ProveedorView, ProveedorNew, ProveedorEdit, proveedores_inactivar
from . import views



app_name = 'compras'

urlpatterns = [

    path('', ProveedorView.as_view(),name='proveedores_list'),
    path('new/', ProveedorNew.as_view(),name='proveedores_new'),
    path('edit/<int:pk>', ProveedorEdit.as_view(),name='proveedores_edit'),
    path('inactivar/<int:pk>',views.proveedores_inactivar, name='proveedores_inactivar')





]
