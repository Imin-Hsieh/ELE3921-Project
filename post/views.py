from django.shortcuts import render, redirect, get_object_or_404
from profile_page.models import Category
from .models import Post, Answer, Rating
from .forms import PostForm, AnswerForm
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.http import JsonResponse

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

def submit_answer(request):
    # Redirect to login page if user is not logged in
    if not request.user.is_authenticated:
        messages.error(request, "You have to log in before writing an answer.")
        return redirect("login")
    
    # Redirect to home if user is a normal user or Institution user
    if not request.user.is_professional:
        messages.error(request, f"You can only write posts as a professional user. Your account is a \"{request.user.get_account_type_display()}\" account.")
        return redirect("home")
    
    # get the post
    post_id = request.POST.get("post_id")
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False) # set author and post before saving
            answer.author = request.user.professional_profile
            answer.post = post
            answer.save()
            messages.success(request, "Your answer was successfully published!")
            return redirect(reverse("view_post", kwargs={"post_id" : post_id}))
    else:
        form = AnswerForm()
    
    context = {
        "title" : post.title,
        "post" : post,
        "form" : form
    }
    return render(request, "post/view_post.html", context=context)


# Creates a rating if none exists
@require_POST
def like_answer(request, answer_id):
    print("WE GOT HEREWE GOT HEREWE GOT HEREWE GOT HEREWE GOT HEREWE GOT HEREWE GOT HERE")
    user = request.user
    answer = Answer.objects.get(id=answer_id)
    post = answer.post

    if not user.is_authenticated:
        messages.error(request, "Error: you must log in.")
        return redirect("login")
    
    if not user.is_professional:
        messages.error(request, "Error: only professional users can rate answers.")
        return redirect(reverse("view_post", kwargs={"post_id" : post.id}))
    
    rating_already_existed = Rating.objects.filter(answer=answer, professional=user.professional_profile).exists()

    if not rating_already_existed:
        rating = Rating.objects.create(answer=answer, professional=user.professional_profile)

    count = answer.ratings.count()

    return JsonResponse({
        "count" : count,
        "already_liked" : rating_already_existed
    })
    
