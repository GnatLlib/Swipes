from django.contrib import admin

# Register your models here.
from .models import Post, PostDate

admin.site.register(Post)
admin.site.register(PostDate)