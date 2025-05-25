from django.db import models
from profile_page.models import UserProfile, ProfessionalProfile
from search.models import Category

# Abstract model for Post and Answer with shared fields
class Info(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    time_posted = models.DateTimeField(auto_now_add=True)
    # note: should NOT be possible to update Posts, so no last_updated time here

    class Meta:
        abstract = True

# The actual question asked by a normal user
class Post(Info):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="posts")
    categories = models.ManyToManyField(Category, related_name="posts")

# An answer to a post, written by a professional user
class Answer(Info):
    author = models.ForeignKey(ProfessionalProfile, on_delete=models.CASCADE, related_name="answers")
    last_updated = models.DateTimeField(auto_now=True)

# A positive rating. Professionals can click to give positive rating to an answer.
class Rating(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name="ratings")
    professional = models.ForeignKey(ProfessionalProfile, on_delete=models.CASCADE, related_name="ratings")
    
    # at the moment, I only allow a "thumbs up" which represents a +1 vote,
    # so I declare this field with default value equal to 1, but this gives
    # the option to change how rating works in the future without too much work.
    value = models.SmallIntegerField(default=1)

    class Meta:
        # Require that the combination of answer and professionalProfile foreign keys are unique.
        # This is so that a professionalProfile cannot rate the same answer more than once.
        constraints = [
            models.UniqueConstraint(fields=["answer", "professional"], name="unique_answer_professional")
        ]