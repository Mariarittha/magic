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
from decimal import Decimal
from django.contrib.messages import get_messages
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
 # Adicione prints para debug
    print("Número de notificações não lidas:", unread_count)
    print("Notificações não lidas:", notifications)

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

def aceitar_reserva(request, estadia_id):
    estadia = get_object_or_404(Estadia, pk=estadia_id)
    # Lógica para aceitar a reserva, como atualizar o status da estadia, enviar mensagem, etc.
    # ...

    # Marcar a notificação como lida
    notification = Notification.objects.filter(user=request.user, estadia=estadia).first()
    if notification:
        notification.is_read = True
        notification.save()

    return redirect('dashboard')

def recusar_reserva(request, estadia_id):
    estadia = get_object_or_404(Estadia, pk=estadia_id)
    # Lógica para recusar a reserva, enviar mensagem, etc.
    # ...

    # Marcar a notificação como lida
    notification = Notification.objects.filter(user=request.user, estadia=estadia).first()
    if notification:
        notification.is_read = True
        notification.save()

    return redirect('dashboard')


class index(generic.TemplateView):
    template_name = "filomenas/index.html"
    
class index_logado(generic.TemplateView):
    template_name = "filomenas/index_logado.html"


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>....
#                                                                        CRUDS

# CRUD DE HOSPEDE

class Criarhospede( generic.CreateView):
    model = Hospede
    form_class = HospedeForm
    template_name = 'filomenas/form_hospede.html'
    success_url = reverse_lazy("listar_perfil")
    success_message = "Perfil criado com sucesso!"

    def form_valid(self, form):
        # Verifica se já existe um Hospede associado ao usuário
        existing_hospede = Hospede.objects.filter(email=self.request.user.email).first()
        if existing_hospede:
            # Se já existir, não cria um novo e redireciona para a página desejada
            messages.warning(self.request, "Perfil já existente.")
            return self.form_invalid(form)
        
        # Se não existir, salva o Hospede associado ao usuário atual
        form.instance.email = self.request.user.email
        return super().form_valid(form)
    
class PerfilView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'filomenas/perfi.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtenha o Hospede associado ao usuário logado
        hospede = Hospede.objects.filter(email=self.request.user.email).first()
        
        if hospede:
            context['hospede'] = hospede

        return context

class ListarPerfil(LoginRequiredMixin, generic.ListView): 
    model = Hospede
    template_name = 'filomenas/perfil.html'
    context_object_name = 'hospedes'

    def get_queryset(self):
        # Retorna apenas o perfil do usuário autenticado
        return Hospede.objects.filter(email=self.request.user.email)
    
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
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        search_valor_min = self.request.GET.get('search_valor_min', None)
        search_valor_max = self.request.GET.get('search_valor_max', None)
        
        if search_valor_min and search_valor_max:
            # Filtrar por valor mínimo e máximo
            queryset = queryset.filter(valor__range=(Decimal(search_valor_min), Decimal(search_valor_max)))
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_valor_min'] = self.request.GET.get('search_valor_min', '')
        context['search_valor_max'] = self.request.GET.get('search_valor_max', '')
        return context

    
class ListarEstadialoga(generic.ListView):
    model = Estadia
    template_name = 'filomenas/listar_pacotes_logado.html'
    context_object_name = 'estadias'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        search_valor_min = self.request.GET.get('search_valor_min', None)
        search_valor_max = self.request.GET.get('search_valor_max', None)
        
        if search_valor_min and search_valor_max:
            # Filtrar por valor mínimo e máximo
            queryset = queryset.filter(valor__range=(Decimal(search_valor_min), Decimal(search_valor_max)))
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_valor_min'] = self.request.GET.get('search_valor_min', '')
        context['search_valor_max'] = self.request.GET.get('search_valor_max', '')
        return context


class CriarEstadia( views.SuccessMessageMixin, generic.CreateView):
    model = Estadia
    form_class = EstadiaForm
    template_name = 'filomenas/form_estadia.html'
    success_url = reverse_lazy("dashboard")
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
    Notification.objects.create(user=request.user, message=f"{estadia.nome}: Sua aquisição de estadia foi notificada. Aguarde a validação de {estadia.filomena}!", is_read=False)

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