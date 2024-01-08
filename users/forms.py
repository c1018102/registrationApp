from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email Address', help_text='Your Student Email Address.')
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), help_text='Your Date of Birth')
    address = forms.CharField(max_length=255, help_text='Your Address')
    city_town = forms.CharField(max_length=100, help_text='Your City/Town')
    country = forms.CharField(max_length=100, help_text='Your Country')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_of_birth', 'address', 'city_town', 'country', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'address', 'city_town', 'country', 'image', 'course', 'module_Selection_1_ID_Number', 'module_Selection_2_ID_Number']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        
        # Add required attribute to specific fields
        self.fields['date_of_birth'].required = True,
        self.fields['address'].required = True
        self.fields['city_town'].required = True
        self.fields['country'].required = True
        self.fields['course'].required = False
        self.fields['module_Selection_1_ID_Number'].required = False
        self.fields['module_Selection_2_ID_Number'].required = False
