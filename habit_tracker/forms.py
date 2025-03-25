from django.forms import ModelForm

from .models import Habit, Incident

class HabitForm(ModelForm):
    class Meta:
        model = Habit
        fields = ('title', 'target')

class IncidentForm(ModelForm):
    class Meta:
        model = Incident
        fields = ('id_habit',)