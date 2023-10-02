from django.db import models
from users.models import User

# Create your models here.

class Performer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='performer')
    genre = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    # image_url = models.ImageField(upload_to='performers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)