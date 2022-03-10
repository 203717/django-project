from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Profile(models.Model):
    id_user_profile = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    img_profile = models.ImageField(upload_to='img_profile/', null=True)

    class Meta:
        db_table = 'TablitaProfile' 