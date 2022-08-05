from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('projects/', get_projects),
    path('projects/<int:id>/', get_project),
    path('tags/<str:name>/', insert_tag),
    path('projects/insert/', insert_project),
    path('projects/delete/<int:pk>/', delete_project),
    path('projects/edit/<int:pk>/', edit_project),
]