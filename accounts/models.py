from django.db import models
from django.contrib.auth.models import AbstractUser



# User model
class User(AbstractUser):
    class Role(models.TextChoices):
        USER = ("user", "User")
        PROFESSIONAL = ("professional", "Professional")
        INSTITUTION = ("institution", "Institution")
        
    account_type = models.CharField(max_length=20, choices=Role.choices)

    @property
    def is_user(self):
        return self.account_type == self.Role.USER
    
    @property
    def is_professional(self):
        return self.account_type == self.Role.PROFESSIONAL
    
    @property
    def is_institution(self):
        return self.account_type == self.Role.INSTITUTION