from django.shortcuts import render,redirect
from .forms import BusquedaForm
from .models import Busqueda,Resultado
from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.


class busqueda(ListView):   
    model = Busqueda
    template_name= 'Busqueda.html'
    

    def get(self, request,*args, **kwargs):
        queryset=Busqueda.objects.filter(usuario=request.user)
        contexto={
            'object_list':queryset
        }
        return render(request, self.template_name, contexto)


class EditarBusqueda(UpdateView):
    model = Busqueda
    template_name = 'crear_busqueda.html'
    form_class= BusquedaForm
    success_url= reverse_lazy('Busquedas')



class CrearBusqueda(CreateView):
    model = Busqueda
    form_class=BusquedaForm
    template_name='crear_busqueda.html'
    
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            Busqueda = form.save(commit=False)  # gives you the instance
            Busqueda.usuario = request.user  # assuming you're using `ForeignKey` here, calling it `user` instead of `username` for clarity
            Busqueda.save()
            return redirect('Busquedas')




class Resultados(ListView):
    model = Resultado
    template_name='resultados.html'
    context_object_name='resultados'
    paginate_by = 15
    
    
    def get_queryset(self):
        
        return Resultado.objects.filter(usuario=self.request.user)

        

class EliminarBusqueda(DeleteView):
    model = Busqueda
    success_url=reverse_lazy('Busquedas')
    template_name = 'busqueda_confirm_delete.html'

