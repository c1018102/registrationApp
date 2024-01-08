from django import forms
from .models import Module

class AddModule(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['name', 'code', 'credit', 'category', 'description', 'availability', 'courses_allowed']

    # You can customize widgets or add help_text for specific fields if needed
    widgets = {
        'availability': forms.Select(choices=[('open', 'Open'), ('closed', 'Closed')]),
    }

class ModuleSelectionForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['users']
        widgets = {'users': forms.CheckboxSelectMultiple}




