from django.urls import path, include
from .views import (
    VenueApiView,
    VenueDetailApiView,
)

urlpatterns = [
    path('venue', VenueApiView.as_view()),
    path('venue/<int:venue_id>', VenueDetailApiView.as_view()),
]