# Django
from django.db import models

# Local
from auths.models import Client


class Search(models.Model):
    """Model for cities."""

    client = models.ForeignKey(
        to=Client, on_delete=models.CASCADE,
        related_name="user_search", verbose_name="пользователь"
    )
    city = models.CharField(
        verbose_name="город", max_length=100, null=False, blank=False
    )
    count = models.BigIntegerField(
        verbose_name="счетчик поиска", default=0, null=False, blank=False
    )

    class Meta:
        ordering = ("-id",)
        verbose_name = "история поиска"
        verbose_name_plural = "история поиска"

    def __str__(self) -> str:
        return f"{self.client} {self.city} {self.count}"
