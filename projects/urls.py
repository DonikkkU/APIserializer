from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('projects/', projects),
    path('projects/<int:pk>/', project_detail),
    path('skill/', skill)
]