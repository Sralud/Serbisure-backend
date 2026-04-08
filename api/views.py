import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from .models import CustomUser, WorkerProfile

def ServiceListView(request):
    """
    Placeholder view for listing services.
    Will be replaced with a full DRF view in Task 3.
    """
    return JsonResponse({
        "status": "success",
        "message": "Service list endpoint is working.",
        "data": []
    })

@csrf_exempt
def RegisterView(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            role = data.get('role', 'homeowner')
            full_name = data.get('full_name', '')
            
            # Basic validation
            if not email or not password:
                return JsonResponse({"error": "Email and password are required"}, status=400)
            
            if CustomUser.objects.filter(email=email).exists():
                return JsonResponse({"error": "Email already exists"}, status=400)
                
            # Create user
            user = CustomUser.objects.create_user(
                username=email, # Using email as username
                email=email,
                password=password,
                role=role,
                full_name=full_name
            )
            
            # Create worker profile if role is service_worker
            if role == 'service_worker':
                WorkerProfile.objects.create(user=user)
                
            return JsonResponse({
                "message": "User registered successfully",
                "user": {
                    "email": email,
                    "role": role,
                    "full_name": full_name
                }
            }, status=201)
            
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    
    return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def LoginView(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            
            # Note: since USERNAME_FIELD is 'email', we authenticate normally.
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                return JsonResponse({
                    "message": "Login successful",
                    "user": {
                        "email": user.email,
                        "role": user.role
                    }
                })
            else:
                return JsonResponse({"error": "Invalid credentials"}, status=401)
                
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
            
    return JsonResponse({"error": "Method not allowed"}, status=405)
