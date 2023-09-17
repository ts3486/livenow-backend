from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Venue
from .serializers import VenueSerializer

class VenueApiView(APIView):
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the venue items for given requested user
        '''

        # use filter to restrict to user's filter: e.g filter(user = request.user.id)
        venues =Venue.objects
        serializer =VenueSerializer(venues, many=True)
        return Response(serializer.data,  status=status.HTTP_200_OK)
    

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
    

class VenueDetailApiView(APIView):
    def get_object(self, venue_id, user_id):
        '''
        Helper method to get the object with given venue_id, and user_id
        '''
        try:
            return Venue.objects.get(id=venue_id, user = user_id)
        except Venue.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, venue_id, *args, **kwargs):
        '''
        Retrieves the Venue with given venue_id
        '''
        venue_instance = self.get_object(venue_id, request.user.id)
        if not venue_instance:
            return Response(
                {"res": "Object with Venue id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = VenueSerializer(venue_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, venue_id, *args, **kwargs):
        '''
        Updates the Venue item with given venue_id if exists
        '''
        venue_instance = self.get_object(venue_id, request.user.id)
        if not venue_instance:
            return Response(
                {"res": "Object with Venue id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = VenueSerializer(instance = venue_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, venue_id, *args, **kwargs):
        '''
        Deletes the Venue item with given venue_id if exists
        '''
        venue_instance = self.get_object(venue_id, request.user.id)
        if not venue_instance:
            return Response(
                {"res": "Object with Venue id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        venue_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )