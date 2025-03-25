from django.db import models

# Create your models here.
class Habit(models.Model):

    TARGET = (
        (None, 'выберите цель'),
        ('30', 'Каждый день'),
        ('15', 'Каждые 2 дня'),
        ('12', '3 раза в неделю'),
        ('8', '2 раза в неделю'),
        ('4', 'Каждую неделю'),
        ('1', 'Каждый месяц'),
    )

    title = models.CharField(max_length=300, verbose_name='Название')
    target = models.CharField(max_length=16, choices=TARGET, verbose_name='Частота привычки')
    date = models.DateField(auto_now=False, auto_now_add=True, verbose_name='Дата появления привычки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'привычки'
        verbose_name = 'привычка'
        ordering = ['date']


class Incident(models.Model):
    
    id_habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='incidents', verbose_name='id привычки')
    date = models.DateField(auto_now=False, auto_now_add=True, verbose_name='дата события')

    class Meta:
        verbose_name_plural = 'события'
        verbose_name = 'событие'
        ordering = ['date']
