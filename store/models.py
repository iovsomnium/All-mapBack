from django.db import models

# Create your models here.
class store(models.Model):
    storeRegion = models.CharField(max_length = 200)
    storeName = models.CharField(max_length = 200)
    storeFloor = models.IntegerField()
    lat = models.DecimalField(max_digits=11, decimal_places=8)
    lng = models.DecimalField(max_digits=11, decimal_places=8)
    storeImg = models.ImageField(null=True)