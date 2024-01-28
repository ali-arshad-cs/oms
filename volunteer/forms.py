from django import forms
from .models import Volunteer


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = '__all__'
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'date_joined': forms.DateInput(attrs={'type': 'date'}),
            'date_left': forms.DateInput(attrs={'type': 'date'}),
        }
