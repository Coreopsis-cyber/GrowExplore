from django.db import models


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length = 128)
    username = models.CharField(max_length = 128)
    email = models.CharField(max_length = 128)
    Streaks = models.CharField(max_length = 9999, default = 0)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username

