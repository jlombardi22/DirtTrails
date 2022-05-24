from django.urls import path
from end_trails import views


urlpatterns = [
    path('', views.user_end_point),
    path('all/', views.get_all_end_points),
    path('<pk>/', views.end_point_detail),
]
