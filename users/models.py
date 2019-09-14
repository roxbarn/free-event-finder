from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # username = models.CharField(max_length=50)
    # first_name = models.CharField(max_length=50)
    # surname = models.CharField(max_length=50)
    # email = models.EmailField()

  def __str__(self):
    return self.email
