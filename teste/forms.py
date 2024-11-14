from django import forms
from django.shortcuts import render

from teste.models import usuarios, tarefas

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = usuarios
        fields = '__all__'


class TarefaForm(forms.ModelForm):
    class Meta:
        model = tarefas
        fields = '__all__'

