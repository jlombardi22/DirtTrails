from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,  IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404

from .serializers import EndTrailSerializer
from .models import EndTrail
# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_end_points(request):
    end_trails = EndTrail.objects.all()
    serializer = EndTrailSerializer(end_trails, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_end_point(request):

    if request.method == 'POST':
        serializer = EndTrailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        end_trails = EndTrail.objects.filter(trail_id=request.trail.id)
        serializer = EndTrailSerializer(end_trails, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def end_point_detail(request, pk):
    end_trail = get_object_or_404(EndTrail, pk=pk)
    if request.method == 'GET':
        serializer = EndTrailSerializer(end_trail)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EndTrailSerializer(end_trail, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        end_trail.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

# def create_end_point(request):
#     if request.method == 'POST':
#         serializer = EndTrailSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
