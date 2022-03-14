from django.contrib import admin
from .models import CustomUser
# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


ADDITIONAL_USER_FIELDS = (
    (None, {'fields': ('login_streak',)}),
)

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELDS
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS

admin.site.register(CustomUser, CustomUserAdmin)