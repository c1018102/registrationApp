from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm (UserCreationForm):
    email = forms.EmailField(label= 'Email Address', help_text= 'Your Student Email Address.')    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
