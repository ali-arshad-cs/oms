# guardians/models.py
from django.db import models


class Guardian(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    cnic = models.TextField(blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    relationship = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], blank=True, null=True)

    guardian_picture = models.ImageField(upload_to='shared_images/', null=True, blank=True)
    stamp_paper = models.ImageField(upload_to='shared_images/', null=True, blank=True)
    cnic_picture = models.ImageField(upload_to='shared_images/', null=True, blank=True)


    # Your other Guardian model fields and methods

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
