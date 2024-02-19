from django import forms
from .models import PersonLead, ColdCall


class PersonLeadForm(forms.ModelForm):

    class Meta:
        model = PersonLead
        fields = ['name', 'email', 'phone', 'lead_source', 'lead_quality']
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone',
            'lead_source': 'Lead Source',
            'lead_quality': 'Lead Quality',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'lead_source': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'lead_quality': forms.Select(attrs={'class': 'form-control', 'required': True}),
        }


class ColdCallForm(forms.ModelForm):
    class Meta:
        model = ColdCall
        fields = ['caller', 'call_datetime', 'call_duration_minutes', 'status', 'notes', 'follow_up_date', 'lead']
        exclude = ['call_datetime']