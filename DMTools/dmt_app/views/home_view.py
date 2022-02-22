from django.http import HttpResponse
from django.template import loader
from ..services import firebase_service as firebase_service

def home_view(request):
    user_data = firebase_service.FirebaseService.get_user_data("jaimegbonorino@gmail.com", "123321")
    request.session["user_token"] = user_data["token"]
    email = user_data["email"]
    template = loader.get_template("home.html")
    context = {
        "greeting": f"Hi, {email}",
    }
    return HttpResponse(template.render(context, request))