from django import forms
from .models import Post

# Form for registering a new post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # author specified in the view
        fields = ("title", "content", "categories")