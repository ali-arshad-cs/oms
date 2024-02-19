from django.db import models

from oms import settings


class PersonLead(models.Model):
    # Define choices for lead quality
    LEAD_QUALITY_CHOICES = [
        ('strong', 'Strong'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    # Person Lead Information
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    lead_source = models.CharField(max_length=100)
    lead_quality = models.CharField(max_length=20, choices=LEAD_QUALITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ColdCall(models.Model):
    # Caller Information
    caller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    # Call Details
    call_datetime = models.DateTimeField(auto_now_add=True)
    call_duration_minutes = models.PositiveIntegerField()

    # Outcome
    OUTCOME_CHOICES = [
        ('interested', 'Interested'),
        ('not_interested', 'Not Interested'),
        ('follow_up', 'Follow-up Needed'),
        ('no_answer', 'No Answer'),
        ('busy', 'Busy'),
        ('wrong_number', 'Wrong Number'),
        ('dont_call_again', 'Dont Call Again'),
        ('other', 'Other'),
    ]
    status = models.CharField(max_length=20, choices=OUTCOME_CHOICES)
    notes = models.TextField(blank=True)

    # Reminder
    follow_up_date = models.DateField(blank=True, null=True)

    # Relationship
    lead = models.ForeignKey(PersonLead, on_delete=models.CASCADE, related_name='cold_calls')

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cold Call - - {self.call_datetime}"
