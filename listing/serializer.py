from rest_framework.serializers import ModelSerializer
from .models import Listings

class ListingSerializer(ModelSerializer):
    class Meta:
        model= Listings
        fields= "__all__"