from django.contrib import messages
from django.http import JsonResponse
from django.views import generic
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from django.urls import reverse_lazy
from django.contrib.messages import views
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EstadiaForm, ProdutosForm, HospedeForm, FilomenasForm
from .models import Estadia, Produtos, Filomenas, Hospede
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Notification
from django.shortcuts import render
from django.contrib import messages

from django.contrib.messages import get_messages
# views.py - notifications
from django.contrib import messages
from django.http import JsonResponse

@login_required
def get_notification_count(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    unread_count = notifications.count()
    return JsonResponse({'unread_count': unread_count})
@login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    unread_count = notifications.count()

    # Marcar as notificações como lidas
    for notification in notifications:
        notification.mark_as_read()

    # Usar SessionStorage para obter mensagens
    storage = messages.get_messages(request)

    reservation_notification = [msg for msg in storage if 'reservation' in msg.tags]

    if reservation_notification:
        # Criar uma nova instância de Notification para a reserva
        Notification.objects.create(user=request.user, message=reservation_notification[0].message, is_read=False)
        unread_count += 1

    return render(request, 'filomenas/notifications.html', {'notifications': notifications, 'unread_count': unread_count})

class index(generic.TemplateView):
    template_name = "filomenas/index.html"
    
class index_logado(generic.TemplateView):
    template_name = "filomenas/index_logado.html"


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>....
#                                                                        CRUDS

# CRUD DE HOSPEDE

class Criarhospede( views.SuccessMessageMixin, generic.CreateView):
    model = Hospede
    form_class = HospedeForm
    template_name = 'filomenas/form_hospede.html'
    success_url = reverse_lazy("listar_perfil")
    success_message = "Perfil criado com sucesso!"

class ListarPerfil(generic.ListView ):
    model = Hospede
    template_name = 'filomenas/perfil.html'
    context_object_name = 'hospedes'
    
class Detalharperfil(generic.DetailView):
    model = Hospede
    template_name = 'filomenas/perfil.html'
    
class Editarperfil( LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = Hospede
    form_class = HospedeForm
    template_name = 'filomenas/form_hospede.html'
    success_url = reverse_lazy("listar_perfil")
    success_message = "Perfil atualizada com sucesso!"
   
# class ListarEstadia( generic.ListView):
#     model = Estadia
#     template_name = 'filomenas/listar_pacotes.html'
#     context_object_name = 'estadias'
#     paginate_by = 3

#  ---------------------------------------------------------------------------------------------------------------   
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
    success_url = reverse_lazy("listar_log")
    success_message = "Estadia cadastrada com sucesso!"

class AtualizarEstadia( LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = Estadia
    form_class = EstadiaForm
    template_name = "filomenas/form_estadia.html"
    success_url = reverse_lazy("dashboard")
    success_message = "Estadia atualizada com sucesso!"
    
class ApagarEstadia( LoginRequiredMixin, generic.DeleteView):
    model = Estadia
    success_url = reverse_lazy("dashboard")
    success_message = "Estadia removida com sucesso!"
    
class DetalharEstadia(generic.DetailView):
    model = Estadia
    template_name = 'filomenas/detalhar.html'
    
class DetalharEstadialoga(generic.DetailView):
    model = Estadia
    template_name = 'filomenas/detalhar_logado.html'
    
def reservar_estadia(request, estadia_id):
    estadia = Estadia.objects.get(pk=estadia_id)

    # Lógica para reservar a estadia...

    # Adicione a mensagem de sucesso

    # Crie a instância de Notification
    Notification.objects.create(user=request.user, message=f"Sua aquisição de estadia foi notificada. Aguarde a validação de {estadia.filomena}!", is_read=False)

    return render(request, 'filomenas/detalhar_logado.html', {'estadia': estadia})
    
class dashboardestadia(LoginRequiredMixin, generic.ListView):
    model = Estadia
    template_name = 'filomenas/dashboard.html'
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
    model = Filomenas
    template_name = 'filomenas/listar_filomenas.html'
    context_object_name = 'filomenas'
    paginate_by = 3
    
class Listarfilom_nao( generic.ListView):
    model = Filomenas
    template_name = 'filomenas/listar_filomena_nao.html'
    context_object_name = 'filomenas'
    paginate_by = 3
    
class contato_log(generic.TemplateView):
    template_name = "filomenas/contato_log.html"
    
class contato(generic.TemplateView):
    template_name = "filomenas/contato.html"
    
class nos_log(generic.TemplateView):
    template_name = "filomenas/sobrenos_log.html"
    
class nos(generic.TemplateView):
    template_name = "filomenas/sobrenos.html"