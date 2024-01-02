from django import forms
from .models import Orphan
from guardians.models import Guardian


class OrphanForm(forms.ModelForm):
    class Meta:
        model = Orphan
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['guardian'].queryset = Guardian.objects.all()
        self.fields['guardian'].label_from_instance = lambda obj: f"{obj.first_name} {obj.last_name}"
        self.fields['siblings'].widget.attrs['class'] = 'form-select'
        self.fields['siblings'].widget.attrs['multiple'] = 'multiple'
        self.fields['siblings'].queryset = Orphan.objects.exclude(id=self.instance.id)
        self.fields['siblings'].label_from_instance = lambda obj: f"{obj.first_name} {obj.last_name}"
        self.fields['siblings'].initial = None


