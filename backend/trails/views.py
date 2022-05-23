from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Trail
from .serializers import TrailSerializer
# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_trails(request):
    trails = Trail.objects.all()
    serializer = TrailSerializer(trails, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def user_trails(request):
    if request.method == 'POST':
        serializer = TrailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        trails = Trail.objects.filter(trail_id=request.trail.id)
        serializer = TrailSerializer(trails, many=True)
        return Response(serializer.data)


# def get_by_id(request, pk):
#     trail = Trail.objects.filter(user_id=pk)
#     serializer = TrailSerializer(trail, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
