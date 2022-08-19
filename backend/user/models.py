from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie


class User(AbstractUser):
    sex = models.CharField(max_length=10, null=True)  # null = True 默认值为 null
    province = models.CharField(max_length=30, null=True)
    age = models.CharField(max_length=5, null=True)
