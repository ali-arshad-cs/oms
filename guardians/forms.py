from django import forms
from .models import Guardian


class GuardianForm(forms.ModelForm):
    class Meta:
        model = Guardian
        fields = '__all__'