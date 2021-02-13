from .models import photos
from rest_framework.serializers import ModelSerializer

class GallerySerializer(ModelSerializer):
    class Meta:
        model = photos
        fields = '__all__'
