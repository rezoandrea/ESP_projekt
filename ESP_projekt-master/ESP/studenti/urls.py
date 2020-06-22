from django.urls import path
from . import views 

urlpatterns = [
    path('studenti/', views.studenti, name='ESP-studenti'),
    
]