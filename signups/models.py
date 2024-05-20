from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class CustomUser(AbstractUser):
    student_id = models.CharField(max_length=9)
    name = models.CharField(max_length=20)
    groups = models.ManyToManyField(
        Group,
        verbose_name = ('groups'),
        blank = True,
        related_name = 'customuser_groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name = ('user permissions'),
        blank = True,
        related_name = 'customuser_user_permissions',
    )