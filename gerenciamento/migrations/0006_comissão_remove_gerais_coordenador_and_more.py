# Generated by Django 4.1.7 on 2023-02-24 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0005_remove_gerais_comissão_gerais_coordenador_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comissão',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordenador', models.CharField(blank=True, choices=[('Jeferson Oliveira', 'Jeferson Oliveira'), ('Elidomar Santos', 'Elidomar Santos'), ('Isac Diogo', 'Isac Diogo'), ('José Santana', 'José Santana'), ('Abel Correia', 'Abel Correia'), ('Geraldo Xavier', 'Geraldo Xavier')], max_length=60, null=True)),
                ('secretário', models.CharField(blank=True, choices=[('Jeferson Oliveira', 'Jeferson Oliveira'), ('Elidomar Santos', 'Elidomar Santos'), ('Isac Diogo', 'Isac Diogo'), ('José Santana', 'José Santana'), ('Abel Correia', 'Abel Correia'), ('Geraldo Xavier', 'Geraldo Xavier')], max_length=60, null=True)),
                ('serviço', models.CharField(blank=True, choices=[('Jeferson Oliveira', 'Jeferson Oliveira'), ('Elidomar Santos', 'Elidomar Santos'), ('Isac Diogo', 'Isac Diogo'), ('José Santana', 'José Santana'), ('Abel Correia', 'Abel Correia'), ('Geraldo Xavier', 'Geraldo Xavier')], max_length=60, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='gerais',
            name='coordenador',
        ),
        migrations.RemoveField(
            model_name='gerais',
            name='secretário',
        ),
        migrations.RemoveField(
            model_name='gerais',
            name='serviço',
        ),
    ]
