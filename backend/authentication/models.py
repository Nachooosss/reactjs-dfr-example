from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=150, unique=True)


REQUIRED_FIELDS = ['username', 'password', "id", "last_login",
                   "is_superuser", "is_staff", "is_active", "date_joined"]
