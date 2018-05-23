from django import forms
from django.forms import ModelForm, DateTimeInput, HiddenInput
from .models import *

class EntryForm(ModelForm):
    class Meta:
        model = formEntries
        fields = '__all__'

class MarksForm(ModelForm):
    class Meta:
        model = MarkValues
        fields = '__all__'
