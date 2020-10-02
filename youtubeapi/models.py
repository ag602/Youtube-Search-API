from django.db import models

# Create your models here.

class Vidata(models.Model):
    videoid = models.CharField(max_length=20, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description= models.CharField(max_length=1000, null=True, blank=True)
    publishedAt = models.CharField(max_length=30, null=True, blank=True)
    thumbnail_medium = models.CharField(max_length=300, null=True, blank=True)
    channeltitle = models.CharField(max_length=100, null=True, blank=True)
    viewcount = models.CharField(max_length=40, null=True, blank=True)
    likecount = models.CharField(max_length=40, null=True, blank=True)
    dislikecount = models.CharField(max_length=40, null=True, blank=True)
    videourl = models.CharField(max_length=40, null=True, blank=True)