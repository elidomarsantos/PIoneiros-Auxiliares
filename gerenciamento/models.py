from django.db import models

APROVADO = (
    ('Sim', 'Sim'),
    ('Não', 'Não'),
 
)

ANUNCIADO = (
    ('Sim', 'Sim'),
    ('Não', 'Não'),
 
)


TEMPO = (
    ('Sim', 'Sim'),
    ('Não', 'Não'),
 
)

COMISSÃO = (
    ('Jeferson Oliveira', 'Jeferson Oliveira'),
    ('Elidomar Santos', 'Elidomar Santos'),
    ('Isac Diogo', 'Isac Diogo'),
    ('José Santana', 'José Santana'),
    ('Abel Correia', 'Abel Correia'),
    ('Geraldo Xavier', 'Geraldo Xavier'),
 
)

MESES = (
    ("Janeiro","Janeiro"),
    ("Fevereiro","Fevereiro"),
    ("Março","Março"),
    ("Abril","Abril"),
    ("Maio","Maio"),
    ("Junho","Junho"),
    ("Julho","Julho"),
    ("Agosto","Agosto"),
    ("Setembro","Setembro"),
    ("Outubro","Outubro"),
    ("Novembro","Novembro"),
    ("Dezembro","Dezembro"),



    
 
)

class Gerais(models.Model):
  
    nome = models.CharField(max_length=60, blank=True, null=True,)
    aprovado =  models.CharField(max_length=60, blank=True, null=True, choices=APROVADO)
    anunciado =  models.CharField(max_length=60, blank=True, null=True, choices=ANUNCIADO)
    mês_Inicial =  models.CharField(max_length=60, blank=True, null=True, choices=MESES)
    mês_Final =  models.CharField(max_length=60, blank=True, null=True, choices=MESES)
    ano_Inicial = models.IntegerField(blank=True, null=True, verbose_name='Ano')
    ano_Final = models.IntegerField(blank=True, null=True, verbose_name='Ano')
    tempo_indeterminado = models.CharField(max_length=60, blank=True, null=True, choices=TEMPO)
    data = models.DateField(blank=True, null=True)
    
    
class Comissão(models.Model)  :
    coordenador = models.CharField(max_length=60, blank=True, null=True, choices=COMISSÃO)
    secretário = models.CharField(max_length=60, blank=True, null=True, choices=COMISSÃO)
    serviço = models.CharField(max_length=60, blank=True, null=True, verbose_name='Superintendente de Serviço', choices=COMISSÃO)  