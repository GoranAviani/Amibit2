from django.db import models
from django.conf import settings
# Create your models here.

class Link(models.Model):
    link_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    link_name = models.CharField(max_length=200)
    link_url = models.CharField(max_length=1000)

    def __str__(self):
        return self.link_name