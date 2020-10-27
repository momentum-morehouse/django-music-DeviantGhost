from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100,null=True, blank=False)
    artist = models.CharField(max_length=50,null=True, blank=False)
    year_release = models.DateField(null=True, blank=False)