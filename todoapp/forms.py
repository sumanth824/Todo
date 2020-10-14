from django import forms
from django.forms import ModelForm
from .models import *

class listform(forms.ModelForm):
    class Meta:
        model = listapp
        fields = ['content','Done']



