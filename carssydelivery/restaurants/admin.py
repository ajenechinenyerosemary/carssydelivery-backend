from django.contrib import admin

# Register your models here.
from .models import Restaurants

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_url', 'cuisine', 'description', 'price', 'available')
    search_fields = ('name', 'cuisine', 'description', 'price')

admin.site.register(Restaurants, RestaurantAdmin)
    
