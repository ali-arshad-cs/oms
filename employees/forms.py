# employees/forms.py

from django import forms
from .models import MonthlySalary, Employee


class MonthlySalaryForm(forms.ModelForm):
    class Meta:
        model = MonthlySalary
        fields = '__all__'

    employee = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'