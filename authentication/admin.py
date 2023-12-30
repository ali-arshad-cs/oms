from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    # Customize the way CustomUser is displayed in the admin
    # list_display = ('id','username', 'first_name', 'last_name','user_type','phone_number',
    #                 'email', 'is_staff', 'is_active', 'date_joined', 'date_of_birth','last_login', 'is_superuser',
    #                 'address')
    search_fields = ('username', 'email')


# Register the CustomUser model with the admin site
admin.site.register(CustomUser, CustomUserAdmin)