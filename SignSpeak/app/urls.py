from django.contrib import admin
from django.urls import path
from . import views
base64_pattern = r'(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$'
urlpatterns = [
    path('text-to-asl/', views.textToAsl, name="textToAsl"),
    path('asl-to-text/', views.AslToText, name="AslToText"),
    
]