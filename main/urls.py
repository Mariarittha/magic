
from django.contrib import admin
from django.urls import path
from filomenas import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index.as_view(), name='home'),

]
