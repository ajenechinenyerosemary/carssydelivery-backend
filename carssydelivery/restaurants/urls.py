from django.urls import path
from .views import getRestaurants,add_Restaurant,edit_Restaurant,delete_Restaurant


urlpatterns = [
  path('getRestaurants/', getRestaurants, name="getRestaurants"),
  path('add_Restaurant/', add_Restaurant, name="add_Restaurant"),
  path('edit_Restaurant/', edit_Restaurant, name="edit_Restaurant"),
  path('delete_Restaurant/', delete_Restaurant, name="delete_Restaurant")
]