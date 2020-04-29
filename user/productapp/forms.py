from django import forms
from .models import *
from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields = '__all__'
