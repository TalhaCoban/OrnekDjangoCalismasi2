from django.urls import path
from . import views


app_name = "RouteGeometry"

urlpatterns = [
    path('HorizontalRG/', views.Horizontal_Route_Geometry, name="Horizontal_Route_Geometry"),
    path('VerticalRG/', views.Vertical_Route_Geometry, name="Horizontal_Route_Geometry"),
    path('TransitionCurves/', views.Transition_Curves, name="Transition_Curves"),

]