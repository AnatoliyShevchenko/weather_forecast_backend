# Django
from django.contrib import admin

# Local
from .models import Search


@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    """Admin panel for custom searching class."""

    model = Search
    list_display = ("client", "city", "count")
    list_filter = ("client", "city", "count")
