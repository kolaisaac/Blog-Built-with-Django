from django.shortcuts import render

# Create your views here.

def home_view(request):
    car = "Toyota"
    return render(
        request,
        "home.html",
        {"car": car}
    )