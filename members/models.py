from datetime import date

from django.db import models

from oms import settings


class Member(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    STATUS_CHOICES = [
        ('A', 'Active'),
        ('I', 'Inactive'),
    ]

    POSITION_CHOICES = [
        ('president', 'President'),
        ('vice_president', 'Vice President'),
        ('2nd_vice_president', '2nd Vice President'),
        ('general_secretary', 'General Secretary'),
        ('joint_secretary', 'Joint Secretary'),
        ('publication_secretary', 'Publication Secretary'),
        ('finance_secretary', 'Finance Secretary'),
        ('executive_member', 'Executive Member'),
        ('general_member', 'General Member'),
    ]

    # Personal Information
    full_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cnic = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)

    # Membership Information
    member_id = models.AutoField(primary_key=True)
    date_joined = models.DateField(null=True, blank=True)
    date_left = models.DateField(null=True, blank=True)
    responsibility = models.CharField(max_length=50)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    membership_status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    # Additional Information
    occupation = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='shared_images/', null=True, blank=True)
    emergency_contact_number = models.CharField(max_length=100, null=True, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.full_name

    def time_spent(self):
        if self.date_joined is None:
            return "Invalid admission date"

        if not isinstance(self.date_joined, date):
            return "Invalid admission date"

        if self.date_left is not None:
            if not isinstance(self.date_left, date):
                return "Invalid discharge date"

            end_date = self.date_left
        else:
            end_date = date.today()

        years = end_date.year - self.date_joined.year
        months = end_date.month - self.date_joined.month

        if end_date.day < self.date_joined.day:
            months -= 1

        if months < 0:
            years -= 1
            months += 12

        year_unit = "Year" if years == 1 else "Years"
        month_unit = "month" if months == 1 else "months"

        if years > 0:
            return f"{years} {year_unit} and {months} {month_unit}"
        else:
            return f"{months} {month_unit}"
