# Rest Framework
from rest_framework import serializers

# Local
from .models import Search


class SearchSerializer(serializers.Serializer):
    """Serializer for validate info."""

    city = serializers.CharField(
        min_length=3, max_length=50, required=True
    )
    days = serializers.IntegerField(
        min_value=0, max_value=3, write_only=True
    )


class CitiesSerializer(serializers.Serializer):
    """Serializer for view search history."""

    city = serializers.CharField(
        max_length=100, required=True
    )
    count = serializers.IntegerField(
        max_value=1000, min_value=1, read_only=True
    )
        