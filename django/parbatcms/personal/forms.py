from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, label= "USER Name")
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(label="Password")
    password2 = forms.CharField(label="Password Again")
