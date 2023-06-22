from django.contrib.auth.models import AbstractUser, UserManager, User
from django.db import models


class RegisteredUsers(AbstractUser):
    username = models.CharField(max_length=30, unique=True, null=True)
    email = models.EmailField(null=True, unique=True)
    password = models.CharField(max_length=40, unique=True)
    objects = UserManager()
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'email']

    def __str__(self):
        return self.username
