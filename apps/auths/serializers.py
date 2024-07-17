# Rest Framework
from rest_framework import serializers

# Local
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    """Serializer for the client."""

    class Meta:
        model = Client
        fields = ("username", "email")


class RegistrationSerializer(serializers.Serializer):
    """Serializer for registration."""

    username = serializers.CharField(
        max_length=32, min_length=6, required=True
    )
    email = serializers.EmailField(
        required=True, max_length=50, min_length=10
    )
    password = serializers.CharField(
        required=True, max_length=32, min_length=8
    )
