from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class UserManager():
    pass

class User(AbstractBaseUser, models.Model):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=1500, null=True, blank=True)
    job_position = models.CharField(max_length=255, default='Employee', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.first_name}'
