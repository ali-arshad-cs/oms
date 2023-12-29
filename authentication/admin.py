from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    # Customize the way CustomUser is displayed in the admin
    list_display = ('username', 'email', 'user_type', 'is_active')
    search_fields = ('username', 'email')


# Register the CustomUser model with the admin site
admin.site.register(CustomUser, CustomUserAdmin)