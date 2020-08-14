from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreation
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreation
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'age', 'sex', 'is_staff']


admin.site.register(CustomUser, CustomUserAdmin)
