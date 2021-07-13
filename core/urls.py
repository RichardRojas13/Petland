from django.urls import path 
from .views import index, LoUsRe, registroUser,formAddClientes, addClientes, verificacionUser, doSuscripcion, cerrarSesion, suscripcionUsuario, desSuscripcion, mantenedorClientes,  formUpdClientes, updClientes, listadoCompras, obtenerDatosCompraProducto

urlpatterns = [
    path('', LoUsRe, name="LoUsRe.html"),
    path('verificacionUser', verificacionUser, name="verificacionUser"),
    path('registroUser',registroUser, name="registroUser"),
    path('index',index, name="index.html"),
    path('index/doSuscripcion/', doSuscripcion, name="donarSuscripcion.html"),
    path('suscripcionUsuario', suscripcionUsuario, name="suscripcionUsuario"),
    path('desSuscripcion', desSuscripcion, name="desSuscripcion"),
    path('cerrarSesion', cerrarSesion, name="cerrarSesion"),
    path('listadoCompras/', listadoCompras, name="listadoCompras.html"),
    path('obtenerDatosCompraProducto', obtenerDatosCompraProducto, name="obtenerDatosCompraProducto"),
    path('mantenedorClientes/', mantenedorClientes, name="mantenedorClientes.html"),
    path('formAddClientes/', formAddClientes, name="formAddClientes.html"),
    path('addClientes', addClientes, name="addClientes"),
    path('formUpdClientes', formUpdClientes, name="formUpdClientes.html"),
    path('updClientes', updClientes, name="updClientes"),
]