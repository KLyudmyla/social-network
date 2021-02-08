from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # user profile information.
    user = models.OneToOneField(User, related_name="user_profile", on_delete=models.CASCADE)
    last_activity = models.DateTimeField(verbose_name="last activity", null=True, blank=True)


