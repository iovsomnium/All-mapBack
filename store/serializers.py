from rest_framework import serializers
from .models import store

class storeSerializer(serializers.ModelSerializer):
    class Meta:
        model = store
        fields = ('storeRegion','storeName','storeFloor','lat','lng','storeImg')