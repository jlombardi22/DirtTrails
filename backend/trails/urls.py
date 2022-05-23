from django.urls import path
from trails import views

urlpatterns = [
    path('', views.user_trails),
    path('all/', views.get_all_trails),
]
