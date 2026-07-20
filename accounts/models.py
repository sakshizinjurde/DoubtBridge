from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    coins = models.IntegerField(default=100)
    guru_score = models.IntegerField(default=0)

    def __str__(self):
        return self.username
