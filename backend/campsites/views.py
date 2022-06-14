from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Campsite
from .serializer import CampsiteSerializer
# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_campsites(request):
    campsites = Campsite.objects.all()
    serializer = CampsiteSerializer(campsites, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def user_campsites(request):
    if request.method == 'POST':
        serializer = CampsiteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        campsites = Campsite.objects.filter(campsite_id=request.campsite.id)
        serializer = CampsiteSerializer(campsites, many=True)
        return Response(serializer.data)
