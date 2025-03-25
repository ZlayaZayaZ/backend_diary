from django.contrib import admin
from django.urls import path

from .views import index, habit, HabitCreateView, IncidentCreateView

urlpatterns = [
    path('', index, name='index'),
    path('<int:id_habit>/', habit, name='habit'),
    path('add/', HabitCreateView.as_view(), name='add'),
    path('<int:id_habit>/add/', IncidentCreateView.as_view(), name='add_incident')
]