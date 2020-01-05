from django import forms
from .models import Image,Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','likes']
