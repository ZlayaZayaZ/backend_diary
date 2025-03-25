from django.shortcuts import render

from django.http import HttpResponse

from .models import Habit, Incident

from django.views.generic.edit import CreateView
from .forms import HabitForm, IncidentForm
from django.urls import reverse_lazy

class HabitCreateView(CreateView):
    template_name = 'create_habit.html'
    form_class = HabitForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['incidents'] = Incident.oblects.all()
        return context
    
class IncidentCreateView(CreateView):
    template_name = 'create_incident.html'
    form_class = IncidentForm
    success_url = reverse_lazy('habit')

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

def index (request):
    habits = Habit.objects.all()
    context = {'habits': habits,}
    return render(request, 'index_habit.html', context)

def habit (request, id_habit):
    habit_incidents = Incident.objects.filter(id_habit=id_habit)
    habit = Habit.objects.all()
    current_habit = Habit.objects.get(pk=id_habit)
    context = { 'habit_incidents': habit_incidents, 'habit': habit,
               'current_habit': current_habit }
    return render (request, 'habit.html', context)