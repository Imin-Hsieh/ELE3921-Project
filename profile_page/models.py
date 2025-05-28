from django.db import models
from accounts.models import User
from search.models import Category

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")

class ProfessionalProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="professional_profile")
    specializations = models.ManyToManyField(Category, related_name="professionals", blank=True)

class InstitutionProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="institution_profile")
    professionals = models.ManyToManyField(ProfessionalProfile, related_name="institutions", blank=True)