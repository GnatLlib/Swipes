from rest_framework import serializers
from .models import Post, PostDate
from django.contrib.auth import get_user_model


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostDate
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(username=validated_data['username'])
        user.set_password(validated_data['username'])
        user.save()

        return user

    class Meta:
        model = get_user_model()
        fields = ['username', 'password','first_name', 'last_name',]

