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
    target = models.CharField(max_length=16, choices=TARGET)
