from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializers import StartTrailSerializer
from .models import StartTrail
from django.shortcuts import get_object_or_404
# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_start_points(request):
    start_trails = StartTrail.objects.all()
    serializer = StartTrailSerializer(start_trails, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def start_point(request):
    # print(
    #     'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = StartTrailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        start_trails = StartTrail.objects.filter(trail_id=request.trail.id)
        serializer = StartTrailSerializer(start_trails, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def start_point_detail(request, pk):
    start_trail = get_object_or_404(StartTrail, pk=pk)
    if request.method == 'GET':
        serializer = StartTrailSerializer(start_trail)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StartTrailSerializer(start_trail, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        start_trail.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
