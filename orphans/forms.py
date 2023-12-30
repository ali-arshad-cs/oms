from django import forms
from .models import Orphan

class OrphanForm(forms.ModelForm):
    class Meta:
        model = Orphan
        fields = '__all__'
