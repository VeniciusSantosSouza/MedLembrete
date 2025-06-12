from django.db import models





class Medicamento(models.Model):
    nome = models.CharField(max_length=255)
    dosagem = models.FloatField(max_length=100)
    horarios = models.CharField(max_length=255)

