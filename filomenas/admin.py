from django.contrib import admin
from .models import Produtos, Hospede, Filomenas, Estadia

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao')
    search_fields = ('nome',)

@admin.register(Hospede)
class HospedeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'profissao', 'email', 'idade', 'telefone', 'formulario_enviado', 'sobre_mim','frase')
    search_fields = ('nome', 'email')

@admin.register(Filomenas)
class FilomenasAdmin(admin.ModelAdmin):
    list_display = ('filomena', 'idade', 'descricao', 'email', 'telefone',  'sobre_mim','frase')
    search_fields = ('filomena', 'email')

@admin.register(Estadia)
class EstadiaAdmin(admin.ModelAdmin):
    list_display = ('nome','filomena', 'duracao', 'localizacao', 'valor', 'programacao')
    search_fields = ('nome', 'localizacao')

