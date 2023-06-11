from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Venue
from .serializers import VenueSerializer

class VenueApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the venue items for given requested user
        '''
        venues =Venue.objects.filter(user = request.user.id)
        serializer =VenueSerializer(venues, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create theVenue with givenVenue data
        '''
        data = {
            'name': request.data.get('name'), 
            "owner": request.data.get("owner"),
            'user': request.user.id
        }
        serializer =VenueSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
