from django import forms
from .models import Produtos, Hospede, Filomenas, Estadia

class ProdutosForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome', 'preco', 'imagem', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Produto'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preço'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição do Produto'}),
        }

class HospedeForm(forms.ModelForm):
    class Meta:
        model = Hospede
        fields = ['nome', 'profissao', 'email', 'idade', 'imagem', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Hóspede'}),
            'profissao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Profissão'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Idade'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
        }

class FilomenasForm(forms.ModelForm):
    class Meta:
        model = Filomenas
        fields = ['nome', 'idade', 'imagem', 'email', 'telefone', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Idade'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição da Estadia'}),

        }

class EstadiaForm(forms.ModelForm):
    class Meta:
        model = Estadia
        fields = ['imagem', 'duracao', 'nome', 'descricao', 'localizacao', 'valor', 'programacao']
        widgets = {
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'duracao': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duração'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da Estadia'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição da Estadia'}),
            'localizacao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Localização'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor'}),
            'programacao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Programação'}),
        }