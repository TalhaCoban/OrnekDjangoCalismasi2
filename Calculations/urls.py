from django.urls import path
from . import views


app_name = "Calculations"


urlpatterns = [
    path('FundComp/', views.Fundamental_Computations, name="Fundamental_Computations"),
    path('HoLaywPolCoor/', views.Horizontal_layout_with_Polar_Coordinates, name="Horizontal_layout_with_Polar_Coordinates"),
    path('CentErr/', views.Centering_Errors, name="Centering_Errors"),
]
