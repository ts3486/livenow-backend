from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Venue(models.Model):
    name = models.CharField(max_length = 180, default="Tao")
    owner = models.CharField(max_length = 180)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length = 180)
    updated_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.name