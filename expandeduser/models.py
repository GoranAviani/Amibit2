from django.db import models

# Create your models here.
# Create your models here.
from django.contrib.auth.models import AbstractUser


class custom_user(AbstractUser):
    userMobilenumber = models.CharField(max_length=50,null=True, blank=True)
    userAddress = models.CharField(max_length=30,null=True, blank=True)
    userCity = models.CharField(max_length=30,null=True, blank=True)
    userCountry = models.CharField(max_length=30,null=True, blank=True)
    userDoB = models.DateField(null=True, blank=True)
    userSecondEmail = models.EmailField(max_length=50,null=True, blank=True)


    def __str__(self):
        return self.email