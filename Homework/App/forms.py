from django import forms
from .models import User

class FormAdd(forms.Form):
    email    = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'name': 'email'}))
    password = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'name': 'password'}))
    login    = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'name': 'login'}))

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'