from django.db import models
from django.conf import settings
# Create your models here.

class link(models.Model):
    linkUser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    linkName = models.CharField(max_length=200)
    linkUrl = models.CharField(max_length=1000)

    def __str__(self):
        return self.linkName