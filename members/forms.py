from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'date_joined': forms.DateInput(attrs={'type': 'date'}),
            'date_left': forms.DateInput(attrs={'type': 'date'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Populate choices for the dropdown field
            self.fields['position'].choices = Member.POSITION_CHOICES
