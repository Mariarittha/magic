from django.contrib import admin
from django.urls import include, path
from filomenas import views
from main import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), 
    path('notifications/', views.notifications, name='notifications'),
    path('get-notification-count/', views.get_notification_count, name='get_notification_count'),
    path('', views.index.as_view(), name='home'),
    path('index', views.index_logado.as_view(), name='home_logado'),
    
    # paginas estaticas
    path('contato/log', views.contato_log.as_view(), name='contato_log'),
    path('contato/', views.contato.as_view(), name='contato'),
    path('sobrenos/', views.nos.as_view(), name='sobrenos'),
    path('sobrenos/log', views.nos_log.as_view(), name='sobrenos_log'),
    
    # listar
    path('listar', views.ListarEstadia.as_view(), name='listar'),
    path('listar/log', views.ListarEstadialoga.as_view(), name='listar_log'),
    path('perfil/listar', views.ListarPerfil.as_view(), name='listar_perfil'),
    path('listar/filo', views.Listarfilom.as_view(), name='listar_fil'),
    path('listar/filo_nao', views.Listarfilom_nao.as_view(), name='listar_fil_nao'),
    path('dashboard/', views.dashboardestadia.as_view(), name='dashboard'),
    
    # Criar
    path('criar_hospede/', views.Criarhospede.as_view(), name="criar_hosp"),
    path('criar/', views.CriarEstadia.as_view(), name="criar"),
    path('criar_filo/', views.Criarfilomena.as_view(), name="criar_filo"),
    
    # Editar
    path('atualizar_estadia/<int:pk>/', views.AtualizarEstadia.as_view(), name="atualizar_estadia"),
    path('atualizar_perfil/<int:pk>/', views.Editarperfil.as_view(), name="editar_perfil"),
    
    # Apagar
    path('apagar_estadia/<int:pk>/', views.ApagarEstadia.as_view(), name='apagar_estadia'),
    
    # Reservar
    path('reservar-estadia/<int:estadia_id>/', views.reservar_estadia, name='reservar_estadia'),
    
    # Detalhar
    path('detalhar_perfil/<int:pk>/', views.Detalharperfil.as_view(), name="detalhar_perfil"),
    path('detalhar/<int:pk>/', views.DetalharEstadia.as_view(), name="detalhar"),
    path('detalhar_log/<int:pk>/', views.DetalharEstadialoga.as_view(), name="detalhar_log"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
