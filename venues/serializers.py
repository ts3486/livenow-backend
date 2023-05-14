from rest_framework import serializers
from .models import Venue
class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ["name", "status", "created", "updated","reservation", "user"]