from django.urls import path, include
from .views import CategoriaView, CategoriaNew,CategoriaEdit, CategoriaDel, SubCategoriaView, SubCategoriaNew, SubCategoriaEdit, SubCategoriaDel
from .views import MarcaView, MarcaNew, MarcaEdit, marca_inactivar, UnidadMedidaView, UnidadMedidaNew, UnidadMedidaEdit, unidad_medida, ProductoView, ProductoNew
from .views import ProductoEdit
from . import views



app_name = 'inventario'


urlpatterns= [

            # URLs de Categorias
            path('categorias/', CategoriaView.as_view(), name = "categoria"),
            path('categorias/new', CategoriaNew.as_view(), name = "categoria_new"),
            path('categorias/edit/<int:pk>/', CategoriaEdit.as_view(), name = "categoria_edit"),
            path('categorias/del/<int:pk>/', CategoriaDel.as_view(), name = "categoria_del"),

            # URLs de SubCategorias
            path('subcategorias/', SubCategoriaView.as_view(), name = "sub_categoria"),
            path('subcategorias/new', SubCategoriaNew.as_view(), name = "subcategoria_new"),
            path('subcategorias/edit/<int:pk>/', SubCategoriaEdit.as_view(), name = "subcategoria_edit"),
            path('subcategorias/del/<int:pk>/', SubCategoriaDel.as_view(), name = "subcategoria_del"),

            # URLs de Marcas
            path('marcas/', MarcaView.as_view(), name = "marca"),
            path('marcas/new', MarcaNew.as_view(), name = "marca_new"),
            path('marcas/edit/<int:pk>/', MarcaEdit.as_view(), name = "marca_edit"),
            path('marcas/inactivar/<int:pk>/', views.marca_inactivar, name = "marca_inactivar"),


            # URLs de Unidades de Medida
            path('unidadesdemedida/', UnidadMedidaView.as_view(), name = "um"),
            path('unidadesdemedida/new', UnidadMedidaNew.as_view(), name = "um_new"),
            path('unidadesdemedida/new/edit/<int:pk>', UnidadMedidaEdit.as_view(), name = "um_edit"),
            path('unidadesdemedida/new/inactivar/<int:pk>', views.unidad_medida, name = "um_inactivar"),

            #URL's de Producto
            path('productos/', ProductoView.as_view(), name = "producto_list"),
            path('productos/new', ProductoNew.as_view(), name = "producto_new"),
            path('productos/edit/<int:pk>', ProductoEdit.as_view(), name = "producto_edit"),
            path('productos/inactivar/<int:pk>', views.producto_inactivar, name = "producto_inactivar"),




]
