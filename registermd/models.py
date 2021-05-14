from django.db import models

regiao_choices = [
    ('BRASIL', 'BRASIL'),
    ('NORLA', 'NORLA'),
    ('CONOSUR', 'CONOSUR')
]

time_choices = [
    ('A&KT', 'A&KT'),
    ('AS&D, Integration', 'AS&D, Integration'),
    ('AS & D, Integration', 'AS & D, Integration'),
    ('All MD Team', 'All MD Team'),
    ('Corn & Sorghum', 'Corn & Sorghum'),
    ('Crop Protection', 'Crop Protection'),
    ('MDR & FOE', 'MDR & FOE'),
    ('Soybean & Cotton', 'Soybean & Cotton'),
]


# Create your models here.
class Publication(models.Model):
    regiao = models.CharField(max_length=7, choices=regiao_choices, default = 'BRASIL')
    pais = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    time = models.CharField(max_length=100, choices=time_choices, default = 'A&KT')
    email = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    cpf = models.CharField(max_length=200)
    rg = models.CharField(max_length=200)
    data_de_nascimento = models.DateField()
    publication_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
