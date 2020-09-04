from django.shortcuts import render
from django.urls import reverse_lazy

from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import FormularioLogin, FormularioUsuario
from .models import Usuario

from django.views.generic import CreateView, ListView,UpdateView,DeleteView

# Create your views here.

class Login(FormView):
    template_name='login.html'
    form_class=FormularioLogin
    success_url=reverse_lazy('Busquedas')


    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)


    def form_valid(self, form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)



def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect(reverse('inicio'))



class RegistrarUsuario(CreateView):
    model = Usuario
    form_class=FormularioUsuario
    template_name='usuarios/crear_usuario.html'
    success_url=reverse_lazy('login')