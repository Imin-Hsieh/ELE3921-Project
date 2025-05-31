from django.shortcuts import render
from post.models import Post
from profile_page.models import ProfessionalProfile, InstitutionProfile
from django.db.models.functions import Coalesce
from django.db.models import Sum, Value, Count

def home(request):
    posts = Post.objects.order_by("-time_posted")[:5]

    context = {
        "title" : "Home",
        "posts" : posts
    }
    return render(request, "core/home.html", context=context)


def professionals_view(request):
    # get all professionals (also including those with 0 ratings for their answers)
    # and rank them according to amount of ratings. For professionals with the same
    # amount of total ratings, order by their total number of answers.
    professionals = ProfessionalProfile.objects.annotate(
        total_ratings=Coalesce(Sum("answers__ratings__value"), Value(0)),
        answer_count=Coalesce(Count("answers", distinct=True), Value(0))
    ).order_by("-total_ratings", "-answer_count")

    context = {
        "title" : "Professionals",
        "professionals" : professionals
    }
    return render(request, "core/professionals.html", context=context)


def institutions_view(request):
    institutions = InstitutionProfile.objects.annotate(
        total_ratings=Coalesce(Sum("professionals__answers__ratings__value"), Value(0)),
        answer_count=Coalesce(Count("professionals__answers", distinct=True), Value(0))
    ).order_by("-total_ratings", "-answer_count")

    context = {
        "title" : "Professionals",
        "institutions" : institutions
    }
    return render(request, "core/institutions.html", context=context)

