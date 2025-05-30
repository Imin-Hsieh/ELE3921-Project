from django.shortcuts import render, redirect
from accounts.models import User
from profile_page.models import UserProfile, ProfessionalProfile, InstitutionProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from accounts.forms import UserRegistrationForm, ProfessionalRegistrationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST


# Log in
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You were successfully logged in!")
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login_page.html", context={"form" : form, "title" : "Log in"})

# Register a new user and creates a user profile for them
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.account_type = User.Role.USER
            user.save()
            new_profile = UserProfile(user=user)
            new_profile.save()
            messages.success(request, "Registration successful! Log in below.")
            return redirect("login")
    else:
        form = UserRegistrationForm()
    
    return render(request, "accounts/register_page.html", context={"form" : form, "title" : "Register"})

# Log out
def logout_view(request):
    logout(request)
    return redirect("home")


# Register professional
@require_POST
def register_prof(request):
    # Find the institution that attempts to register the professional
    institution_id = request.POST.get("institution_id")
    institution_user = get_object_or_404(User, id=institution_id)
    institution = institution_user.institution_profile

    form = ProfessionalRegistrationForm(request.POST)
    if form.is_valid():
        # Make the User
        user = form.save(commit=False)
        user.account_type = User.Role.PROFESSIONAL
        user.save()
        # Make the User's ProfessionalProfile and set its specializations
        new_prof_profile = ProfessionalProfile.objects.create(user=user)
        new_prof_profile.specializations.set(form.cleaned_data.get("specializations", []))
        new_prof_profile.save()
        # Add the professional to the institution
        institution.professionals.add(new_prof_profile)

        messages.success(request, "Registration successful!")
        return redirect("view_profile", user_id=institution_id)
    
    context = {
        "title" : "Register professional",
        "form" : form,
        "institution_id" : institution_id
    }
    return render(request, "accounts/register_prof_page.html", context=context)