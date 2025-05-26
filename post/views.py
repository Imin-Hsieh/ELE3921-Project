from django.shortcuts import render, redirect, get_object_or_404
from profile_page.models import Category
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.urls import reverse

# Write posts and post them
def write_post(request):
    # Redirect to login page if user is not logged in
    if not request.user.is_authenticated:
        messages.error(request, "You have to log in before writing a post.")
        return redirect("login")
    
    # Redirect to home if user is a Professional or Institution user
    if not request.user.is_user:
        messages.error(request, f"You can only write posts as a normal user. Your account is a \"{request.user.get_account_type_display()}\" account.")
        return redirect("home")
        
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.user_profile
            post.save()
            return redirect(reverse("view_post", kwargs={"post_id" : post.id}))
    else:
        form = PostForm()
    
    context = {
        "title" : "Write post",
        "categories" : Category.objects.all(),
        "form" : form
    }
    return render(request, "post/write_post.html", context=context)


def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {
        "title" : post.title,
        "post" : post
    }
    return render(request, "post/view_post.html", context=context)

def submit_answer(request, post_id):
    pass # need to do something with Form again