# Django
from django.contrib import admin
from django.urls import path

# Rest Framework
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)

# Third-Party
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
)

# Local
from auths.views import ClientView, Registration
from weather.views import WeatherView, CitiesView


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/token/", TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", TokenRefreshView.as_view(),
        name="token_refresh"
    ),
    path("api/v1/reg/", Registration.as_view()),
    path("api/v1/cabinet/", ClientView.as_view()),
    path("api/v1/forecast/", WeatherView.as_view()),
    path("api/v1/cities/", CitiesView.as_view()),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(
        url_name="schema"
    ), name="swagger-ui"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(
        url_name="schema"
    ), name="redoc"),
]
