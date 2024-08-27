from django.db import models

# Create your models here.
class Restaurants(models.Model): 
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    image_url = models.URLField(max_length=200, blank=True)
    menuItems = models.ForeignKey()
    description = models.TextField(blank=True)
    price = models.FloatField()
    available = models.BooleanField(default=True)
    