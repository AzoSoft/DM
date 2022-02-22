from django.http import HttpResponse
from ..services import firebase_service as firebase_service

def home_view(request):
    user_data = firebase_service.FirebaseService.get_user_data("email", "password")
    request.session["user_token"] = user_data["token"]
    email = user_data["email"]
    return HttpResponse(f"Hello, {email}. You're at the DM-Tools home page.")