from django.contrib import admin

# Register your models here.
from .models import Habit, Incident

class HabitAdmin(admin.ModelAdmin):
    list_display = ('title', 'target')
    list_display_links = ('title',)
    search_fields = ('title',)

class IncidentAdmin(admin.ModelAdmin):
    list_display = ('id_habit', 'date',)

admin.site.register(Habit, HabitAdmin)
admin.site.register(Incident, IncidentAdmin)
