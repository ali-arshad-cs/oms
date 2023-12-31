from django.db import models
# from guardians.models import Guardian
# from education.models import Education
# from health.models import HealthRecord
# from leaves.models import Leave


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

    #siblings = models.ManyToManyField('self', blank=True, symmetrical=False)

    #FOREIGN KEYS FIELDS
    # health_record = models.OneToOneField(HealthRecord, on_delete=models.SET_NULL, null=True, blank=True)
    # education_info = models.ForeignKey(Education, on_delete=models.SET_NULL, null=True, blank=True)
    # guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)
    # leaves = models.ManyToManyField(Leave, related_name='orphans', blank=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
