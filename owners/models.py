from django.db import models
from users.models import User

# Create your models here.

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner')
    bio = models.TextField(blank=True)
    # image_url = models.ImageField(upload_to='performers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
