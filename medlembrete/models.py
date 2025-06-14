from django.db import models



class Enfermeira(models.Model):
    nome_enfermeira = models.CharField(max_length=255)
    email_enfermeira = models.CharField(max_length=100)

class Paciente(models.Model):  
    nome_do_paciente = models.CharField(max_length=255)
    idade_do_paciente = models.IntegerField()
    medicamento_paciente = models.CharField(max_length=255)
    via_paciente = models.CharField(max_length=255)
    dose_unidade_paciente = models.CharField(max_length=255)
    frequencia_paciente = models.IntegerField()
    data_paciente = models.DateField()
    horario_paciente = models.TimeField()  
    observacoes_paciente = models.TextField(blank=True, default='')
