from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.

class User(AbstractUser):
    CUSTOMER = "customer"
    VENDOR = "vendor"
    ADMIN = "admin"

    ROLE_CHOICES = [
        (CUSTOMER,"Customer"),
        (VENDOR,"Vendor"),
        (ADMIN,"Admin"),
    ]
    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default=CUSTOMER,)
    objects = CustomUserManager()