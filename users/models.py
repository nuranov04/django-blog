from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )
    nickname = models.CharField(
        max_length=55
    )
    bio = models.TextField()
    image = models.ImageField(
        upload_to='Profile'
    )

    def __str__(self):
        return self.nickname

