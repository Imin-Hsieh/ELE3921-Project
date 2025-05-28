from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ["username", "email", "account_type"]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields" : ("account_type",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields" : ("account_type",)}),)

admin.site.register(User, CustomAdmin)