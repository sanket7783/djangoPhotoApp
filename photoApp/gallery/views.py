from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import photos
from .serializers import GallerySerializer
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend


class GalleryView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        request.data['user']=request.user.pk
        serializer = GallerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageList(generics.ListAPIView):
    queryset = photos.objects.all()
    serializer_class = GallerySerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['user']
    ordering_filters = ['published_date']

class Image(generics.RetrieveUpdateDestroyAPIView):
    queryset = photos.objects.all()
    serializer_class = GallerySerializer



