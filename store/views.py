from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import store
from .serializers import storeSerializer

@api_view(['GET'])
def helloAPI(request):
    return Response("hello motherfucker")

@api_view(['GET'])
def storeInfo(request):
    totalStores = store.objects.all()
    serializer = storeSerializer(list(totalStores), many=True)
    return Response(serializer.data)

@api_view(['POST'])
def storeRegi(request):
    storeRegion = request.POST['storeRegion']
    storeName = request.POST['storeName']
    storeFloor = request.POST['storeFloor']
    lat = request.POST['lat']
    lng = request.POST['lng']
    storeImg = request.POST['storeImg']
