from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import WastePickup

def home(request):
    return render(request, "wasteapp/home.html")


def pickup_request(request):
    if request.method == "POST":
        print(request.POST)

        name = request.POST.get("name")
        waste_type = request.POST.get("waste_type")
        pickup_date = request.POST.get("pickup_date")
        address = request.POST.get("address")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")

        WastePickup.objects.create(
            name=name,
            waste_type=waste_type,
            pickup_date=pickup_date,
            address=address,
            latitude=latitude if latitude else None,
            longitude=longitude if longitude else None,
        )

        return render(request, "wasteapp/success.html")

    return render(request, "wasteapp/pickup.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("/dashboard/")

        return render(request, "wasteapp/login.html", {
            "error": "Invalid username or password"
        })

    return render(request, "wasteapp/login.html")


def dashboard(request):
    pickups = WastePickup.objects.all().order_by("-created_at")

    return render(request, "wasteapp/dashboard.html", {
        "pickups": pickups
    })