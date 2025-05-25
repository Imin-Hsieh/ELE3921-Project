from django.contrib import admin
from .models import Post, Answer, Rating
# Register your models here.

admin.site.register([Post, Answer, Rating])
