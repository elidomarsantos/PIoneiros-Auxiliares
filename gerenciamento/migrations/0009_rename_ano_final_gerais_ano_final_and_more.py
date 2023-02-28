# Generated by Django 4.1.7 on 2023-02-26 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0008_remove_gerais_período_inicial_gerais_ano_final_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gerais',
            old_name='ano_final',
            new_name='ano_Final',
        ),
        migrations.RenameField(
            model_name='gerais',
            old_name='ano_inicial',
            new_name='ano_Inicial',
        ),
        migrations.RemoveField(
            model_name='gerais',
            name='período_final',
        ),
        migrations.AlterField(
            model_name='gerais',
            name='mês_Final',
            field=models.CharField(blank=True, choices=[('Janeiro', 'Janeiro'), ('Fevereiro', 'Fevereiro'), ('Março', 'Março'), ('Abril', 'Abril'), ('Maio', 'Maio'), ('Junho', 'Junho'), ('Julho', 'Julho'), ('Agosto', 'Agosto'), ('Setembro', 'Setembro'), ('Outubro', 'Outubro'), ('Novembro', 'Novembro'), ('Dezembro', 'Dezembro')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='gerais',
            name='mês_Inicial',
            field=models.CharField(blank=True, choices=[('Janeiro', 'Janeiro'), ('Fevereiro', 'Fevereiro'), ('Março', 'Março'), ('Abril', 'Abril'), ('Maio', 'Maio'), ('Junho', 'Junho'), ('Julho', 'Julho'), ('Agosto', 'Agosto'), ('Setembro', 'Setembro'), ('Outubro', 'Outubro'), ('Novembro', 'Novembro'), ('Dezembro', 'Dezembro')], max_length=60, null=True),
        ),
    ]
