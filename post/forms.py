from django import forms
from .models import Post, Answer

# Form for registering a new post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # author specified in the view
        fields = ("title", "content", "categories")

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        # author and post specified in the view
        fields = ("title", "content")