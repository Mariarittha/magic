# Generated by Django 5.0 on 2023-12-21 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filomenas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filomenas',
            name='nome',
        ),
        migrations.AddField(
            model_name='estadia',
            name='filomena',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='filomenas.filomenas'),
        ),
        migrations.AddField(
            model_name='filomenas',
            name='filomena',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='filomenas',
            name='frase',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='filomenas',
            name='sobre_mim',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='hospede',
            name='frase',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='hospede',
            name='sobre_mim',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
