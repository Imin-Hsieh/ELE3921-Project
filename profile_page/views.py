from django.shortcuts import render
from django.shortcuts import get_object_or_404
from accounts.models import User

# Create your views here.
def view_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    context = {
        "title" : user.username,
        "user" : user
    }
    return render(request, "profile_page/profile_page.html", context=context)