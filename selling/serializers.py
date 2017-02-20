from rest_framework import serializers
from .models import Post, PostDate


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostDate
        fields = '__all__'
