from django import forms
from django.db import models
from .models import AddItem
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        email = models.EmailField(max_length=20)
        
        
        fields = ('username','email','password1','password2')

class Additemform(forms.ModelForm):
    class Meta:
        model = AddItem
        fields = '__all__'
        exclude = ['itemlist']
        


        