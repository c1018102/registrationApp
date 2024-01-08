from django import forms
from .models import Module

class AddModule(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['name', 'code', 'credit', 'category', 'description', 'availability', 'courses_allowed']

    # You can customize widgets or add help_text for specific fields if needed
    widgets = {
        'availability': forms.Select(choices=[('Open', 'Open'), ('Closed', 'Closed')]),
    }

class ModuleSelectionForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    course = forms.CharField(max_length=100)
    module_1 = forms.ModelChoiceField(queryset=Module.objects.all(), label='First Module Choice')
    module_2 = forms.ModelChoiceField(queryset=Module.objects.all(), label='Second Module Choice')

    def clean(self):
        cleaned_data = super().clean()
        module_1 = cleaned_data.get('module_1')
        module_2 = cleaned_data.get('module_2')

        if module_1 == module_2:
            raise forms.ValidationError("Please select different modules.")

        return cleaned_data

