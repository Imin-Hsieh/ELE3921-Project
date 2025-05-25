from django.shortcuts import render, redirect
from accounts.models import User
from profile_page.models import UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from accounts.forms import UserRegistrationForm
from django.contrib import messages


# Log in
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
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