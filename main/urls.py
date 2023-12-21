from django.contrib import admin
from django.urls import include, path
from filomenas import views
from main import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index.as_view(), name='home'),
    path('index', views.index_logado.as_view(), name='home_logado'),
    path('accounts/', include('allauth.urls')), 
    path('listar', views.ListarEstadia.as_view(), name='listar'),
    path('listar/log', views.ListarEstadialoga.as_view(), name='listar_log'),
    path('perfil/listar', views.ListarPerfil.as_view(), name='listar_perfil'),
    path('listar/filo', views.Listarfilom.as_view(), name='listar_fil'),
    path('dashbore', views.dashboreestadia.as_view(), name='dashbore'),


    path('criar/', views.CriarEstadia.as_view(), name="criar"),
    path('criar_filo/', views.Criarfilomena.as_view(), name="criar_filo"),

    path('atualizar_estadia/<int:pk>/', views.AtualizarEstadia.as_view(), name="atualizar_estadia"),
    path('detalhar/<int:pk>/', views.DetalharEstadia.as_view(), name="detalhar"),
    path('detalhar_log/<int:pk>/', views.DetalharEstadialoga.as_view(), name="detalhar_log"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
