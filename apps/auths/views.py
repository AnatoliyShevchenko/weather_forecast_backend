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

# Local
from .models import Client
from .serializers import ClientSerializer, RegistrationSerializer


class ClientView(APIView):
    """View for the clients."""

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @staticmethod
    @extend_schema(
        responses={200: ClientSerializer}
    )
    def get(request: Request) -> Response:
        data = ClientSerializer(data=request.user)
        data.is_valid(raise_exception=True)
        return Response(data=data, status=status.HTTP_200_OK)

    @staticmethod
    @extend_schema(
        responses={200: dict, 404: dict}
    )
    def delete(request: Request) -> Response:
        user: Client = request.user
        try:
            user.delete()
            return Response(
                data={"success": "user was removed"},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                data={"error": str(e)}, status=status.HTTP_404_NOT_FOUND
            )


class Registration(APIView):
    """View for Registration users."""

    permission_classes = [AllowAny]

    @staticmethod
    @extend_schema(
        request=RegistrationSerializer,
        responses={200: dict, 400: dict}
    )
    def post(request: Request) -> Response:
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")
        if username == password:
            return Response(
                data={
                    "error": "password must be different from username"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            Client.objects.create_user(
                email=email, username=username, password=password
            )
            return Response(
                data={"success": "registration success"},
                status=status.HTTP_200_OK
            )
