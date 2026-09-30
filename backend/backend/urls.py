from django.contrib import admin
from django.urls import path
from wasteapp.views import home, pickup_request, dashboard, user_login

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("pickup/", pickup_request, name="pickup"),
    path("login/", user_login, name="login"),
    path("dashboard/", dashboard, name="dashboard"),
]