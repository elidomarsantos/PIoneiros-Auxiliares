# Generated by Django 4.1.7 on 2023-02-24 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0003_gerais_comissão_gerais_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gerais',
            name='período',
        ),
        migrations.AddField(
            model_name='gerais',
            name='período_final',
            field=models.DateField(blank=True, null=True, verbose_name='A: (MM/AAAA)'),
        ),
        migrations.AddField(
            model_name='gerais',
            name='período_inicial',
            field=models.DateField(blank=True, null=True, verbose_name='Período de: (MM/AAAA)'),
        ),
    ]
