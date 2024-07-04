from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=40,label="Username",widget=forms.TextInput(attrs={
        'placeholder':'Username',
        'autocomplete':'off'
        }))

    password1 = forms.CharField(max_length=40,label='Password',widget=forms.TextInput(attrs={
        'placeholder':'Password',
        'autocomplete':'off',
        'type':'password',
    }))

    password2 = forms.CharField(max_length=40,label='Password Again',widget=forms.TextInput(attrs={
        'placeholder':'Password',
        'autocomplete':'off',
        'type':'password',
    }))

    link1 = forms.URLField(max_length=40,label='Link1',widget=forms.TextInput(attrs={
        'placeholder':'Link 1',
        'autocomplete':'off',
        'type':'text',
    }))

    link2 = forms.URLField(max_length=40,label='Link2',widget=forms.TextInput(attrs={
        'placeholder':'Link 2',
        'autocomplete':'off',
        'type':'text',
    }))

    link3 = forms.URLField(max_length=40,label='Link3',widget=forms.TextInput(attrs={
        'placeholder':'Link 3',
        'autocomplete':'off',
        'type':'text',
    }))

    link4 = forms.URLField(max_length=40,label='Link3',widget=forms.TextInput(attrs={
        'placeholder':'Link 4',
        'autocomplete':'off',
        'type':'text',
    }))


    class Meta:
        model = User
        fields = ('username','password1','password2','link1','link2','link3','link4')        