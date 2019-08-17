from django.db import models

# Create your models here.
from django.conf import settings


class user_phone(models.Model):
    userMobilePhone = models.ForeignKey(settings.AUTH_USER_MODEL, unique= True, on_delete=models.CASCADE)
    phoneCountryCode = models.CharField(max_length=6)
    phoneNumber = models.CharField(max_length=12)
    isMobileValidated = models.BooleanField(default = False)
    
    def __str__(self):
        return self.phoneNumber