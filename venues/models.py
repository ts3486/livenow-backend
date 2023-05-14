from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    name = models.CharField(max_length = 180),
    owner = models.CharField(max_length = 180),
    created_at = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    status = models.CharField(max_length = 180),
    updated = models.DateTimeField(auto_now = True, blank = True)
    reservation = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.name