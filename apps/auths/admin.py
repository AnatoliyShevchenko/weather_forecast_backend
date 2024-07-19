# Django
from django.contrib import admin

# Local
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Admin panel for custom user's class."""

    model = Client
    list_display = (
        "email", "username", "is_superuser",
    )
    list_filter = ("email", "username")
    search_fields = ("email", "username")
