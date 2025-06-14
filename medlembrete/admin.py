from django.contrib import admin
from .models import Enfermeira
from .models import Paciente

admin.site.register(Enfermeira)
admin.site.register(Paciente)
