from django.contrib import admin
from django.urls import path

from .views import index, diary

urlpatterns = [
    path('', index),
    path('<int:id_diary>/', diary)
]