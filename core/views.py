from django.shortcuts import render
from post.models import Post

def home(request):
    posts = Post.objects.order_by("-time_posted")[:5]

    context = {
        "title" : "Home",
        "posts" : posts
    }
    return render(request, "core/home.html", context=context)