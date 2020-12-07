from django.urls import path, include
from .views import helloAPI,storeInfo

urlpatterns = [
    path('hello/', helloAPI),
    path('all/', storeInfo),
]