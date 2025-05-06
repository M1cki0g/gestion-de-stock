from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your models here.

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Adresse email")
    first_name = forms.CharField(max_length=30, required=True, label="Prénom")
    last_name = forms.CharField(max_length=30, required=True, label="Nom de famille")
    
    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        