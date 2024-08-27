import json
from django.http import JsonResponse 
from datetime import datetime, timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from .utils import create_jwt_token

@csrf_exempt
def register(request):
    if request.method == "POST":
        try:
            json_data = request.body.decode("utf-8")
            data_dict = json.loads(json_data)
            
            username = data_dict.get("username")
            password = data_dict.get("password")
            
            if not username or not password:
                return JsonResponse({"message": "Username and password are required"}, status=400)
            
            if User.objects.filter(username=username).exists():  # Fixed typo from `exist` to `exists`
                return JsonResponse({"message": "User already exists"}, status=400)
            
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return JsonResponse({"message": "Registration Successful"}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON"}, status=400)
        
        except Exception as e:
            return JsonResponse({"message": f"An error occurred: {str(e)}"}, status=500)
    
    return JsonResponse({"message": "Invalid request method"}, status=405)

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        try:
            json_data = request.body.decode("utf-8")
            data_dict = json.loads(json_data)
            
            username = data_dict.get("username")
            password = data_dict.get("password")
            
            if not username or not password:
                return JsonResponse({"message": "Username and password are required"})
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                token = create_jwt_token(user)
                response =  JsonResponse({"message": "Login Successful", "token": token}, status=200)
                response.set_cookie(key='jwt', value=token, httponly=True, )
                # samesite='strict', secure=True, expires=datetime.now(timezone.utc) + datetime.timedelta(hours=1)   
                return response
            else:
                return JsonResponse({"message": "Invalid credentials"}, status=401)
        
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON"}, status=400)
        
        except Exception as e:
            return JsonResponse({"message": f"An error occurred: {str(e)}"}, status=500)
    
    return JsonResponse({"message": "Invalid request method"}, status=405)
