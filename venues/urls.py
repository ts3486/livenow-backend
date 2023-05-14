from django.conf.urls import url
from django.urls import path, include
from .views import (
    VenueApiView,
)

urlpatterns = [
    path('api', VenueApiView.as_view()),
]