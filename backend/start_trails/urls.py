from django.urls import path
from start_trails import views


urlpatterns = [
    path('', views.start_point),
    path('all/', views.get_all_start_points),
    path('<pk>/', views.start_point_detail),
]
