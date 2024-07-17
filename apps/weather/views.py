# Rest Framework
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

# SimpleJWT
from rest_framework_simplejwt.authentication import JWTAuthentication

# Third-Party
from drf_spectacular.utils import extend_schema

# Django
from django.core.cache import cache

# Local
from .utils import get_forecast
from .serializers import SearchSerializer, CitiesSerializer
from .models import Search
from auths.models import Client


class WeatherView(APIView):
    """View for get weather forecast."""

    permission_classes = [AllowAny]

    @extend_schema(
        request=SearchSerializer,
        responses={200: dict, 404: str},
    )
    def post(self, request: Request) -> Response:
        serializer = SearchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        city=serializer.validated_data.get("city")
        days=serializer.validated_data.get("days")
        client = request.user
        if isinstance(client, Client):
            obj = Search.objects.get(client=client)
            if not obj:
                obj = Search(
                    client=client, city=city
                )
                obj.count=1
                obj.save()
            else:
                obj.count += 1
                obj.save(update_fields=["count"])
        cache_key = f"{city}_{days}"
        cached = cache.get(key=cache_key)
        if not cached:
            forecast = get_forecast(city=city, days=days)
            if not forecast:
                return Response(
                    data={"error": "Город не найден"}, 
                    status=status.HTTP_404_NOT_FOUND
                )
            cache.set(key=cache_key, value=forecast, timeout=30*60)
            return Response(
                data={"success": forecast}, status=status.HTTP_200_OK
            )
        return Response(
            data={"success": cached}, status=status.HTTP_200_OK
        )


class CitiesView(APIView):
    """View for get user's search cities."""

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @extend_schema(
        responses={200: CitiesSerializer},
    )
    def get(self, request: Request) -> Response:
        client: Client = request.user
        data = Search.objects.filter(client=client)
        serializer = CitiesSerializer(data=data, many=True)
        return Response(
            data={"success": serializer.data}, status=status.HTTP_200_OK
        )
