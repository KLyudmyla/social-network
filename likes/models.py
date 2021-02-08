from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone

from posts.models import Post


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user.username)
