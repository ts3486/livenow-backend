from django.urls import path, include
from .views import (
    VenueApiView,
    VenueDetailApiView,
)

urlpatterns = [
    path('api', VenueApiView.as_view()),
    path('api/<int:venue_id>', VenueDetailApiView.as_view()),
]