from django import forms
from django.forms import ModelForm, DateTimeInput, HiddenInput
from formentry.submodals.formGenerator import *

class mainForm(ModelForm):
    class Meta:
        model=formValue
        fields = '__all__'
        # widgets = {
        #     'pub_date': DateTimeInput(attrs={'class': 'datetime-input'}),
        #     'creator' : HiddenInput()
        # }

class tableForm(ModelForm):
    class Meta:
        model=headings
        fields = '__all__'

class questionForm(ModelForm):
    class Meta:
        model=questions
        fields = '__all__'

class choiceForm(ModelForm):
    class Meta:
        model=QuestionChoice
        fields = '__all__'
