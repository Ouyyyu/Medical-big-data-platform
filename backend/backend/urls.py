from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("user/", include("user.urls")),
    path("baike/", include("baike.urls")),
    path("robot", include("robot.urls")),
]
