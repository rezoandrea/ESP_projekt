from django.urls import path
from . import views

urlpatterns = [
    path('', views.tvrtke, name='ESP-tvrtke'),
]