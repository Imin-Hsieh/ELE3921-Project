from django.contrib import admin
from .models import UserProfile, ProfessionalProfile, InstitutionProfile
# Register your models here.

admin.site.register([UserProfile, ProfessionalProfile, InstitutionProfile])