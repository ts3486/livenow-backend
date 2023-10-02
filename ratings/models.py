from django.db import models
from users.models import User
from venues.models import Venue

# Create your models here.

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='ratings')
    rating_value = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)