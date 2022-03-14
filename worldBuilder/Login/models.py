from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
# Create your models here.

class CustomUser(AbstractUser):
    class Meta:
        managed = True
        db_table = 'Login_user'
    login_streak = models.IntegerField(default = 0)


