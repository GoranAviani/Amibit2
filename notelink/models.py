from django.db import models
from django.conf import settings
# Create your models here.

class link(models.Model):
    linkUser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    linkName = models.CharField(max_length=200)
    linkUrl = models.CharField(max_length=1000)

    def __str__(self):
        return self.linkName


class Note(models.Model):
    noteUser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    noteTitle = models.CharField(max_length=200)
    noteText = models.TextField()
    noteTimestamp = models.DateTimeField(auto_now_add=True) #auto_now_add time the instance was created
    noteSlug = models.SlugField(max_length=250)
    
    def __str__(self):
        return self.noteTitle