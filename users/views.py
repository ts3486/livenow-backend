from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

# Create your views here.

class RegisterView(APIView):
    def get(self, request, *args, **kwargs):
        users = User.objects
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data,  status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
