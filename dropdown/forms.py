from django import forms
from dropdown.models import DropdownModel

class DropdownModelForm(forms.ModelForm):
    class Meta:
        model = DropdownModel
        fields = ('date_range','event',)
        widgets = {
            'date_range': forms.Select(choices=DropdownModel.CHOICES)
        }