from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=15
    )
    image = models.ImageField(
        blank=True, null=True,
    )
    description = models.TextField()
    create_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

    def get_parent(self):
        return self.comment.filter(parent__isnull=True)

    class Meta:
        ordering = ('-id',)


class Subscribe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribe_user')
