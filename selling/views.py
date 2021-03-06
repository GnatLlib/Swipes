from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, PostDate
from .forms import PostForm
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import PostSerializer, PostDateSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model



# ///////////////////////////////////// VIEWS FOR TESTING PURPOSES \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
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

''' Non-generic API class
class PostList(APIView):

    def get(self,request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

# ///////////////////////////REST API IMPLEMENTATION HERE\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Using generic API classes


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDateList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = PostDate.objects.all()
    serializer_class = PostDateSerializer


class PostDateDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = PostDate.objects.all()
    serializer_class = PostDateSerializer

# //////////////////////// USER CREATION API \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


class CreateUserView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer



