from django.db import models
from django.contrib.auth.models import AbstractUser



# User model
class User(AbstractUser):
    class Role(models.TextChoices):
        USER = ("user", "User")
        PROFESSIONAL = ("professional", "Professional")
        INSTITUTION = ("institution", "Institution")
        
    account_type = models.CharField(max_length=20, choices=Role.choices)