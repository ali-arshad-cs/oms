# models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    USER_TYPES = (
        ('administrator', 'Administrator'),
        ('member', 'Member'),
        ('financial_officer', 'Financial Officer'),
        ('volunteer', 'Volunteer'),
        ('donor', 'Donor'),
        ('manager', 'Manager'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='member')
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    def is_administrator(self):
        return self.user_type == 'administrator'

    def is_member(self):
        return self.user_type == 'member'

    def is_financial_officer(self):
        return self.user_type == 'financial_officer'

    def is_volunteer(self):
        return self.user_type == 'volunteer'

    def is_donor(self):
        return self.user_type == 'donor'

    def is_manager(self):
        return self.user_type == 'manager'

    def get_user_type_display(self):
        return dict(self.USER_TYPES)[self.user_type]
