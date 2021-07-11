from django.urls import path 
from .views import index, LoUsRe, registroUser, verificacionUser

urlpatterns = [
    path('', LoUsRe, name="LoUsRe.html"),
    path('verificacionUser', verificacionUser, name="verificacionUser"),
    path('registroUser',registroUser, name="registroUser"),
    path('index',index, name="index.html"),
]