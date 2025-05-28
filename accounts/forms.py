from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import User
from post.models import Category
from profile_page.models import ProfessionalProfile, InstitutionProfile

# Custom form for registering a new user
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name")
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("An account is already registered with this email.")
        return email
    

# New form for professionals because they have specializations and affiliated institutions
class ProfessionalRegistrationForm(UserRegistrationForm):
    specializations = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        required=False
    )
    institutions = forms.ModelMultipleChoiceField(
        queryset=InstitutionProfile.objects.all(),
        required=False # In case a professional may be able to register without an institution in the future, but not possible now
    )