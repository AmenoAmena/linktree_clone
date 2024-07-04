from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    link1 = models.URLField()
    link2 = models.URLField(blank=True)
    link3 = models.URLField(blank=True)
    link4 = models.URLField(blank=True)




