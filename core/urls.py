from django.urls import path, re_path
from . import views
from .views import AltaProductoView

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto', views.contacto, name='contacto'),
    #path('productos/alta', views.alta_producto, name='alta_producto'), esta es la que iba pero la quiero reemplazar por una CBV, por lo que la ruta va a ser la de abajo
    path('alta_producto/', AltaProductoView.as_view(), name='alta_producto'),
    path('personajes/alta', views.alta_personaje, name='alta_personaje'),
    path('compañias/alta', views.alta_empresa, name='alta_compañia'),
    path('listado_productos', views.listar_productos, name='listado_productos'), #cambiar el primero a productos/listado
    path('personajes/listado', views.listar_personajes, name='listado_personajes'),
    path('compañias/listado', views.listar_empresas, name='listado_compañias'),

]
