# leave/models.py

from django.db import models

from oms import settings
from orphans.models import Orphan


class Leave(models.Model):
    orphan = models.ForeignKey(Orphan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    notes = models.TextField(blank=True, null=True)
    went_with = models.CharField(max_length=100, blank=True, null=True, verbose_name="Person Went With")
    arrived_with = models.CharField(max_length=100, blank=True, null=True, verbose_name="Person Arrived With")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)


def __str__(self):
        return f"Leave for {self.orphan.first_name} {self.orphan.last_name} - {self.start_date} to {self.end_date}"
