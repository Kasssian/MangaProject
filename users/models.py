from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser, UserManager
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class RegisteredUsers(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True, null=True, help_text='Enter your name')
    email = models.EmailField(null=True, unique=True, help_text='Enter your nickname')
    password = models.CharField(max_length=40, unique=True, help_text='Enter your password')
    objects = UserManager()
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'email']

    def __str__(self):
        return self.username
