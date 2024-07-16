# Django
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, Group, Permission,
)
from django.db import models
from django.core.exceptions import ValidationError


class ClientManager(BaseUserManager):
    """Manager for Clients."""

    def create_user(
        self, email: str, username: str, password: str
    ) -> "Client":
        """Registration user."""

        if not email:
            raise ValidationError("Email required")

        user: "Client" = self.model(
            email=self.normalize_email(email),
        )
        user.username = username
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self, email: str, username: str, password: str
    ) -> "Client":
        """Create admin."""

        user: "Client" = self.model(
            email=self.normalize_email(email),
        )
        user.username = username
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class Client(AbstractBaseUser, PermissionsMixin):
    """Model for Clients."""

    email = models.EmailField(
        max_length=100, unique=True, verbose_name="почта"
    )
    username = models.CharField(
        max_length=20, verbose_name="имя пользователя", unique=True
    )
    # is_active = models.BooleanField(
    #     default=False, verbose_name="активность"
    # )
    is_superuser = models.BooleanField(
        default=False, verbose_name="администратор"
    )
    # is_staff = models.BooleanField(
    #     default=False, verbose_name="менеджер"
    # )
    groups = models.ManyToManyField(
        Group,
        related_name="client_set",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="client_permissions_set",
        blank=True
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = ClientManager()

    class Meta:
        ordering = ("-id",)
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self) -> str:
        return f"{self.username} {self.email}"
