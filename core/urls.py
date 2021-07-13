from django.urls import path 
from .views import index, LoUsRe, registroUser, verificacionUser, doSuscripcion, cerrarSesion, suscripcionUsuario, desSuscripcion

urlpatterns = [
    path('', LoUsRe, name="LoUsRe.html"),
    path('verificacionUser', verificacionUser, name="verificacionUser"),
    path('registroUser',registroUser, name="registroUser"),
    path('index',index, name="index.html"),
    path('index/doSuscripcion/', doSuscripcion, name="donarSuscripcion.html"),
    path('suscripcionUsuario', suscripcionUsuario, name="suscripcionUsuario"),
    path('desSuscripcion', desSuscripcion, name="desSuscripcion"),
    path('cerrarSesión', cerrarSesion, name="cerrarSesión"),
]