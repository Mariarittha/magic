from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def mark_as_read(self):
        self.is_read = True
        self.save()


class Produtos(models.Model):
    nome = models.CharField(max_length=120)
    preco = models.FloatField()
    imagem = models.ImageField(null=True)
    descricao = models.CharField(max_length=1000)

class Hospede(models.Model):
    nome = models.CharField(max_length=120)
    profissao = models.CharField(max_length=120)
    email = models.EmailField(null=True)
    idade = models.IntegerField()
    imagem = models.ImageField(null=True)
    telefone = models.CharField(max_length=20, null=True)
    formulario_enviado = models.BooleanField(default=False)
    sobre_mim = models.CharField(max_length=400, null=True)
    frase = models.CharField(max_length=300, null=True)

class Filomenas(models.Model):
    filomena = models.CharField(max_length=120, null=True)
    idade = models.IntegerField()
    descricao = models.CharField(max_length=1000)
    imagem = models.ImageField(null=True)
    email = models.EmailField(null=True)
    sobre_mim = models.CharField(max_length=400, null=True)
    frase = models.CharField(max_length=300, null=True)
    telefone = models.CharField(max_length=20, null=True) 
    def __str__(self):
        if self.filomena:
            return self.filomena
        else:
            return f"Filomena-{self.filomena}"
    
class Estadia(models.Model):
    filomena = models.ForeignKey(Filomenas, on_delete=models.CASCADE, null=True)
    imagem = models.ImageField(null=True)
    duracao = models.IntegerField()
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=1000)
    localizacao = models.CharField(max_length=500)
    valor = models.DecimalField(verbose_name=("valor"), decimal_places=2, max_digits=6)    
    programacao = models.CharField(max_length=1000, null=True)

    