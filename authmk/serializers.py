from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.response import Response
from .tokens import get_access_token, get_refresh_token


class LoginEmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=5)
    password = serializers.CharField(min_length=8, max_length=30)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password')


