
from django.contrib import admin
from django.urls import include, path
from filomenas import views
from main import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index.as_view(), name='home'),
    path('accounts/', include('allauth.urls')), 


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
