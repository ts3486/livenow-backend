from django.db import models

# Create your models here.

class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ratings')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='ratings')
    rating_value = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)