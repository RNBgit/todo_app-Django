from dataclasses import field
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

        widgets = {

            'title': forms.TimeInput(attrs={'class': 'form-control'})
        }