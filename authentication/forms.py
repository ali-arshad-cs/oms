# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('user_type', 'profile_picture','first_name', 'last_name', 'email', 'bio', 'date_of_birth', 'address', 'phone_number')
        user_type = forms.ChoiceField(choices=CustomUser.USER_TYPES)