from django import forms
from .models import PersonLead, ColdCall


class PersonLeadForm(forms.ModelForm):

    class Meta:
        model = PersonLead
        fields = '__all__'


class ColdCallForm(forms.ModelForm):
    class Meta:
        model = ColdCall
        fields = ['caller', 'call_datetime', 'call_duration_minutes', 'status', 'notes', 'follow_up_date', 'lead']
        exclude = ['call_datetime']