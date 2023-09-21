from django.db import models

# Create your models here.

class Performer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='performer')
    genre = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    image_url = models.ImageField(upload_to='performers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)