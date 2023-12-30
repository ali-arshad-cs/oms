from django.contrib import admin
from .models import Orphan


class OrphanAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


admin.site.register(Orphan, OrphanAdmin)
