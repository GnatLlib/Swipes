from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.http import Http404


def index(request):
    all_posts = Post.objects.all()

    return render(request, "index.html", {"title": "home", "list": all_posts})


def list_post(request):
    if not request.user.is_authenticated():
        raise Http404

    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()

    return render(request, "create.html", {"title": "create", "form": form})


def view_post(request):

    return render(request, "index.html", {"title": "view"})


def delete_post(request, id):
    instance = get_object_or_404(Post, id=id)
    instance.delete()

    return redirect("index")

