from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    coins = models.IntegerField(default=100)
    guru_score = models.IntegerField(default=0)

    role = models.CharField(
        max_length=20,
        choices=[
            ('student', 'Student'),
            ('guru', 'Guru')
        ],
        default='student'
    )

    bio = models.TextField(blank=True)
    skills = models.TextField(blank=True)

    def __str__(self):
        return self.username