from django.db import models
from accounts.models import User
from search.models import Category

# Create your models here.

class ProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

class UserProfile(ProfileInfo):
    pass

class ProfessionalProfile(ProfileInfo):
    specializations = models.ManyToManyField(Category, related_name="professionals")

class InstitutionProfile(ProfileInfo):
    professionals = models.ManyToManyField(ProfessionalProfile, related_name="institutions")