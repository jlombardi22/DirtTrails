from django.urls import path
from start_trails import views


urlpatterns = [
    path('all/', views.get_all_start_points),
    path('', views.start_point),
]
