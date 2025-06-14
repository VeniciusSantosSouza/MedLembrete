from django import forms
from .models import Enfermeira
from .models import Paciente

class EnfermeiraForm(forms.ModelForm):
    class Meta:
        model = Enfermeira
        fields = '__all__'
        widgets = {
            'nome_enfermeira': forms.TextInput(),
            'email_enfermeira': forms.EmailInput(),
        }

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'nome_do_paciente': forms.TextInput(),
            'idade_do_paciente': forms.NumberInput(),
            'medicamento_paciente': forms.TextInput(),
            'via_paciente': forms.TextInput(),
            'dose_unidade_paciente': forms.TextInput(),
            'frequencia_paciente': forms.NumberInput(),
            'data_paciente': forms.DateInput(attrs={'type': 'date'}),
            'horario_paciente': forms.TimeInput(attrs={'type': 'time'}),
            'observacoes_paciente': forms.Textarea(),
        }
