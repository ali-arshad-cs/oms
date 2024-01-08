from django.contrib.auth.models import User
from django.db import models
from guardians.models import Guardian  # Import Guardian here
from datetime import date

from oms import settings


class Orphan(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    STATUS_CHOICES = [
        ('onboard', 'Onboard'),
        ('discharged', 'Discharged'),
    ]

    FAMILY_STATUS_CHOICES = [
        ('father_died', 'Father Died'),
        ('mother_died', 'Mother Died'),
        ('both_parents_died', 'Both Parents Died'),
        ('broken_family', 'Broken Family'),
        ('poor_family', 'Poor Family'),
        ('single_parent', 'Single Parent'),
        ('orphanage_care', 'Orphanage Care'),
        ('living_with_relatives', 'Living with Relatives'),
        ('abandoned', 'Abandoned'),
        ('adopted', 'Adopted'),
        ('divorced_parents', 'Divorced Parents'),
        ('separated_parents', 'Separated Parents'),
        ('unknown', 'Unknown'),
        ('other', 'Other'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    address = models.TextField()
    notes = models.TextField()
    family_status = models.CharField(max_length=25, choices=FAMILY_STATUS_CHOICES, null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    ethnicity = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    religion = models.CharField(max_length=50, null=True, blank=True)
    language = models.CharField(max_length=50, null=True, blank=True)
    admission_date = models.DateField(null=True, blank=True)
    discharge_date = models.DateField(null=True, blank=True)
    hobbies = models.TextField(null=True, blank=True)
    special_needs = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, blank=True)
    orphan_picture = models.ImageField(upload_to='shared_images/', null=True, blank=True)
    admission_form_picture = models.ImageField(upload_to='shared_images/', null=True, blank=True)
    bform_picture = models.ImageField(upload_to='shared_images/', null=True, blank=True)
    picture_at_time_of_admission = models.ImageField(upload_to='shared_images/', null=True, blank=True)
    siblings = models.ManyToManyField('self', blank=True, symmetrical=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    #FOREIGN KEYS FIELDS
    guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE, related_name='orphans', null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    # health_record = models.OneToOneField(HealthRecord, on_delete=models.SET_NULL, null=True, blank=True)
    # education_info = models.ForeignKey(Education, on_delete=models.SET_NULL, null=True, blank=True)
    # guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)
    # leaves = models.ManyToManyField(Leave, related_name='orphans', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - (
                    (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))


    def time_spent(self):
        if self.admission_date is None:
            return "Invalid admission date"

        if not isinstance(self.admission_date, date):
            return "Invalid admission date"

        if self.discharge_date is not None:
            if not isinstance(self.discharge_date, date):
                return "Invalid discharge date"

            end_date = self.discharge_date
        else:
            end_date = date.today()

        years = end_date.year - self.admission_date.year
        months = end_date.month - self.admission_date.month

        if end_date.day < self.admission_date.day:
            months -= 1

        if months < 0:
            years -= 1
            months += 12

        year_unit = "Year" if years == 1 else "Years"
        month_unit = "month" if months == 1 else "months"

        return f"{years} {year_unit} and {months} {month_unit}"