# from django.http import JsonResponse
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# import json

# from .models import Restaurants
# from user.utils import decode_jwt_token

# # Create your views here.

# @csrf_exempt
# def getRestaurants(request):
#     if request.method == 'GET':
#         # auth_header = request.headers.get('Authorization')
#         # if auth_header and auth_header.startswith('Bearer '):
#         #     token = auth_header.split('Bearer ')[1]
#         #     is_valid = decode_jwt_token(token)
#         #     if is_valid in ["Invalid Token", "Token Expired"]:
#         #         return JsonResponse({"error": "Invalid or expired token"}, status=401)



#         restaurants = Restaurants.objects.all()


#         restaurant_list = list(restaurants.values())
#         return JsonResponse({
#             "message": "Get restaurant route is active",
#             "data": restaurant_list
#         })
#     else:
#         return JsonResponse({"message": "Invalid method"}, status=405)

# @csrf_exempt
# def add_Restaurant(request):
#     if request.method == "POST":
#         try:
#             json_data = request.body.decode("utf-8")
#             data_dict = json.loads(json_data)
#         except json.JSONDecodeError:
#             return JsonResponse({"error": "Invalid JSON"}, status=400)

#         restaurant_name = data_dict.get("name")
#         if not restaurant_name:
#             return JsonResponse({"error": "Restaurant name is required"}, status=400)

#         existing_restaurant = Restaurants.objects.filter(name=restaurant_name).first()
#         if existing_restaurant:
#             return JsonResponse({"message": "Restaurant with this name already exists"}, status=400)

#         Restaurants.objects.create(**data_dict)
#         return JsonResponse({"message": "Restaurant added successfully"}, status=201)
#     else:
#         return JsonResponse({"message": "Invalid method"}, status=405)

# @csrf_exempt
# def edit_Restaurant(request):
#     if request.method == "PUT":
#         try:
#             json_data = request.body.decode("utf-8")
#             data_dict = json.loads(json_data)
#         except json.JSONDecodeError:
#             return JsonResponse({"error": "Invalid JSON"}, status=400)

#         restaurant_id = data_dict.get("restaurant_id")
#         if not restaurant_id:
#             return JsonResponse({"error": "Restaurant ID is required"}, status=400)

#         try:
#             restaurant = Restaurants.objects.get(id=restaurant_id)
#         except Restaurants.DoesNotExist:
#             return JsonResponse({"message": "Restaurant not found"}, status=404)

#         if "name" in data_dict:
#             restaurant.name = data_dict["name"]
#         if "logo" in data_dict:
#             restaurant.logo = data_dict["logo"]
#         if "description" in data_dict:
#             restaurant.description = data_dict["description"]
#         # if "image" in data_dict:
#         #     restaurant.image = data_dict["image"]
#         if "cuisine" in data_dict:
#             restaurant.cuisine = data_dict["cuisine"]
#         if "price" in data_dict:
#             restaurant.price = data_dict["price"]
#         if "available" in data_dict:
#             restaurant.available = data_dict["available"]
        
#         restaurant.save()
#         return JsonResponse({"message": "Restaurant updated successfully"}, status=200)
#     else:
#         return JsonResponse({"message": "Invalid method"}, status=405)

# @csrf_exempt
# def delete_Restaurant(request):
#     if request.method == "DELETE":
#         try:
#             json_data = request.body.decode("utf-8")
#             data_dict = json.loads(json_data)
#         except json.JSONDecodeError:
#             return JsonResponse({"error": "Invalid JSON"}, status=400)

#         restaurant_id = data_dict.get("restaurant_id")
#         if not restaurant_id:
#             return JsonResponse({"error": "Restaurant ID is required"}, status=400)

#         try:
#             restaurant = Restaurants.objects.get(id=restaurant_id)
#             restaurant.delete()
#             return JsonResponse({}, status=204)
#         except Restaurants.DoesNotExist:
#             return JsonResponse({"message": "Restaurant not found"}, status=404)
#     else:
#         return JsonResponse({"message": "Invalid method"}, status=405)


from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Restaurants
from user.utils import decode_jwt_token

@csrf_exempt
def getRestaurants(request):
    if request.method == 'GET':
        restaurants = Restaurants.objects.all()
        restaurant_list = list(restaurants.values())
        return JsonResponse({
            "message": "Get restaurant route is active",
            "data": restaurant_list
        })
    else:
        return JsonResponse({"message": "Invalid method"}, status=405)

@csrf_exempt
def add_Restaurant(request):
    if request.method == "POST":
        try:
            json_data = request.body.decode("utf-8")
            data_dict = json.loads(json_data)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        restaurant_name = data_dict.get("name")
        if not restaurant_name:
            return JsonResponse({"error": "Restaurant name is required"}, status=400)

        existing_restaurant = Restaurants.objects.filter(name=restaurant_name).first()
        if existing_restaurant:
            return JsonResponse({"message": "Restaurant with this name already exists"}, status=400)

        Restaurants.objects.create(**data_dict)
        return JsonResponse({"message": "Restaurant added successfully"}, status=201)
    else:
        return JsonResponse({"message": "Invalid method"}, status=405)

@csrf_exempt
def edit_Restaurant(request):
    if request.method == "PUT":
        try:
            json_data = request.body.decode("utf-8")
            data_dict = json.loads(json_data)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        restaurant_id = data_dict.get("restaurant_id")
        if not restaurant_id:
            return JsonResponse({"error": "Restaurant ID is required"}, status=400)

        try:
            restaurant = Restaurants.objects.get(id=restaurant_id)
        except Restaurants.DoesNotExist:
            return JsonResponse({"message": "Restaurant not found"}, status=404)

        if "name" in data_dict:
            restaurant.name = data_dict["name"]
        if "logo" in data_dict:
            restaurant.logo = data_dict["logo"]
        if "description" in data_dict:
            restaurant.description = data_dict["description"]
        if "cuisine" in data_dict:
            restaurant.cuisine = data_dict["cuisine"]
        if "price" in data_dict:
            restaurant.price = data_dict["price"]
        if "available" in data_dict:
            restaurant.available = data_dict["available"]
        
        restaurant.save()
        return JsonResponse({"message": "Restaurant updated successfully"}, status=200)
    else:
        return JsonResponse({"message": "Invalid method"}, status=405)

@csrf_exempt
def delete_Restaurant(request):
    if request.method == "DELETE":
        try:
            json_data = request.body.decode("utf-8")
            data_dict = json.loads(json_data)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        restaurant_id = data_dict.get("restaurant_id")
        if not restaurant_id:
            return JsonResponse({"error": "Restaurant ID is required"}, status=400)

        try:
            restaurant = Restaurants.objects.get(id=restaurant_id)
            restaurant.delete()
            return JsonResponse({}, status=204)
        except Restaurants.DoesNotExist:
            return JsonResponse({"message": "Restaurant not found"}, status=404)
    else:
        return JsonResponse({"message": "Invalid method"}, status=405)






