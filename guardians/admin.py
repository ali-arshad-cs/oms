from django.contrib import admin
from .models import Guardian


class GuardianAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


admin.site.register(Guardian, GuardianAdmin)
from django.contrib import admin

# Register your models here.
