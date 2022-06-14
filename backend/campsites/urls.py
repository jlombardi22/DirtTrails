from django.urls import path
from campsites import views

urlpatterns = [
    path('', views.user_campsites),
    path('all/', views.get_all_campsites),
]
