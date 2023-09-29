from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm): 
    
    username = forms.CharField(
        max_length=100, 
        required = True, 
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'username'})
    )

    first_name = forms.CharField(
        max_length=100, 
        required = True, 
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'})
    )

    last_name = forms.CharField(
        max_length=100, 
        required = True, 
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'})
    )
    
    password1 = forms.CharField(
        max_length=100, 
        required = True, 
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Password', 'type':'password'})
    )

    password2 = forms.CharField(
        max_length=100, 
        required = True, 
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Confirm Password', 'type':'password'})
    )

    email = forms.EmailField(
        max_length=100, 
        required = True, 
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email'})
    )

    check = forms.BooleanField(
        required=False,
    )    
        
    class Meta:        
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'check']

    