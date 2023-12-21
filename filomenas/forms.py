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
        fields = ['nome', 'profissao', 'email', 'idade', 'imagem', 'telefone','sobre_mim' ,'frase']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Hóspede'}),
            'profissao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Profissão'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Idade'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
            'sobre_mim': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ex: Gosto muito de ler'}),
            'frase': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ex: Amou daquela vez como se fosse a última.. '}),

        }

class FilomenasForm(forms.ModelForm):
    class Meta:
        model = Filomenas
        fields = ['filomena', 'idade', 'imagem', 'email', 'telefone', 'descricao', 'sobre_mim','frase']
        widgets = {
            'filomena': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Idade'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição da Estadia'}),
            'sobre_mim': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ex: Gosto muito de ler'}),
            'frase': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ex: Amou daquela vez como se fosse a última.. '}),

        }

class EstadiaForm(forms.ModelForm):
    class Meta:
        model = Estadia
        fields = ['filomena','imagem', 'duracao', 'nome', 'descricao', 'localizacao', 'valor', 'programacao']
        widgets = {
            'filomena': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'duracao': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duração'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da Estadia'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição da Estadia'}),
            'localizacao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Localização'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor'}),
            'programacao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Programação'}),
        }
