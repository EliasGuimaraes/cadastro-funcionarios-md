from django.db import models

# Create your models here.
class Publication(models.Model):
    regiao = models.TextField()
    pais = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefone = CharField(max_length=200)
    cpf = CharField(max_length=200)
    rg = CharField(max_length=200)
    data_de_nascimento = models.DateField()
    publication_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)