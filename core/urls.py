from django.urls import path 
from .views import index, LoUsRe, registroUser, verificacionUser, donarSuscripcion, cerrarSesion

urlpatterns = [
    path('', LoUsRe, name="LoUsRe.html"),
    path('verificacionUser', verificacionUser, name="verificacionUser"),
    path('registroUser',registroUser, name="registroUser"),
    path('index',index, name="index.html"),
    path('donarSuscripcion', donarSuscripcion, name="donarSuscripcion.html"),
    path('cerrarSesion', cerrarSesion, name="cerrarSesion"),
]