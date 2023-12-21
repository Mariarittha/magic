from django.contrib import messages
from django.http import JsonResponse
from django.views import generic
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from django.urls import reverse_lazy
from django.contrib.messages import views
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EstadiaForm, ProdutosForm, HospedeForm, FilomenasForm
from .models import Estadia, Produtos, Filomenas, Hospede


class index(generic.TemplateView):
    template_name = "filomenas/index.html"
    
class index_logado(generic.TemplateView):
    template_name = "filomenas/index_logado.html"
 
# logado


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>....
#                                                                        CRUDS

class ListarPerfil( TemplateView):
    template_name = 'filomenas/perfil.html'
   

# CRUD de Estadia
class ListarEstadia( generic.ListView):
    model = Estadia
    template_name = 'filomenas/listar_pacotes.html'
    context_object_name = 'estadias'
    paginate_by = 3
    
class ListarEstadialoga( generic.ListView):
    model = Estadia
    template_name = 'filomenas/listar_pacotes_logado.html'
    context_object_name = 'estadias'
    paginate_by = 3

class CriarEstadia( views.SuccessMessageMixin, generic.CreateView):
    model = Estadia
    form_class = EstadiaForm
    template_name = 'filomenas/form_estadia.html'
    success_url = reverse_lazy("listar")
    success_message = "Estadia cadastrada com sucesso!"

class AtualizarEstadia( LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = Estadia
    form_class = EstadiaForm
    template_name = "filomenas/form_estadia.html"
    success_url = reverse_lazy("listar")
    success_message = "Estadia atualizada com sucesso!"
    
class DetalharEstadia(generic.DetailView):
    model = Estadia
    template_name = 'filomenas/detalhar.html'
    
class DetalharEstadialoga(generic.DetailView):
    model = Estadia
    template_name = 'filomenas/detalhar_logado.html'
    
class dashboreestadia(LoginRequiredMixin, generic.ListView):
    model = Estadia
    template_name = 'filomenas/dashbore.html'
    context_object_name = 'estadias'
    paginate_by = 3    
    
# CRUD DE HOSPEDE

class Criarfilomena(views.SuccessMessageMixin, generic.CreateView):
    model = Filomenas
    form_class = FilomenasForm
    template_name = 'filomenas/form_filomena.html'
    success_url = reverse_lazy("listar_fil")
    success_message = "filomena cadastrada com sucesso!"
    
class Listarfilom( generic.ListView):
    model = Estadia
    template_name = 'filomenas/listar_filomenas.html'
    context_object_name = 'filomenas'
    paginate_by = 3