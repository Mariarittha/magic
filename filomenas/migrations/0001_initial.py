# Generated by Django 4.2.3 on 2023-12-19 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estadia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(null=True, upload_to='')),
                ('duracao', models.IntegerField()),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=1000)),
                ('localizacao', models.CharField(max_length=500)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='valor')),
                ('programacao', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Filomenas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('idade', models.IntegerField()),
                ('descricao', models.CharField(max_length=1000)),
                ('imagem', models.ImageField(null=True, upload_to='')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('telefone', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('profissao', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('idade', models.IntegerField()),
                ('imagem', models.ImageField(null=True, upload_to='')),
                ('telefone', models.CharField(max_length=20, null=True)),
                ('formulario_enviado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('preco', models.FloatField()),
                ('imagem', models.ImageField(null=True, upload_to='')),
                ('descricao', models.CharField(max_length=1000)),
            ],
        ),
    ]
