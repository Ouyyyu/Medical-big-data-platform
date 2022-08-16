from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    sex = models.CharField(max_length=10, null=True)
    province = models.CharField(max_length=30, null=True)
    old = models.CharField(max_length=5, null=True)
