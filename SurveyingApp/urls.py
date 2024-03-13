from django.contrib import admin
from django.urls import path, include

from MainPage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("Calculations/", include("Calculations.urls")),
    path("RouteGeometry/", include("RouteGeometry.urls")),
]
