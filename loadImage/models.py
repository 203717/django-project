from django.utils import timezone
from distutils.command.upload import upload
from django.db import models

# Create your models here.
class ImagenModelo(models.Model):
    url_img = models.ImageField(upload_to='img/', null=False)
    name_img = models.CharField(max_length=255, null=True)    
    format_img = models.CharField(max_length=40,null=True)
    created = models.DateTimeField(default=timezone.now)
    edit = models.DateTimeField(blank=True, null=True, default=None)