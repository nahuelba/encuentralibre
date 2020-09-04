from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import RegistrarUsuario

urlpatterns=[
    path('registrar_usuario/',RegistrarUsuario.as_view(), name='registrar_usuario')
]