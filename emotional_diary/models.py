from django.db import models
from django.forms import ImageField
# Create your models here.


class Situation(models.Model):
    rating_of_the_situation = models.IntegerField(verbose_name='Оценка ситуации') 
    #сделать это поле как выбор из 10 целочисленных вариантов? Не изменяемым в последствии? убрать это поле вовсе?

    description = models.CharField(max_length=300, verbose_name='Описание ситуации')
    conclusions = models.CharField(max_length=300, verbose_name='Выводы')
    body_reaction = models.CharField(max_length=300, verbose_name='Реакция тела')
    img = models.ImageField(blank=True, verbose_name='изображение, отражающее чувства')
    created_at = models.DateField(auto_now=False, auto_now_add=True, verbose_name = 'дата ситуации')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'ситуации'
        verbose_name = 'ситуация'


class Emotion(models.Model):
    EMOTIONS = (
        (None, 'выберите эмоцию'),
        ('fear', 'страх'),
        ('apathy', 'апатия'),
        ('pain', 'боль'),
        ('negation', 'отрицание'),
        ('anger', 'гнев'),
        ('disappointment', 'разочарование'),
        ('sadness', 'печаль'),
        ('admiration', 'восхищение'),
        ('joy', 'радость'),
        ('happiness', 'счастье'),
        ('excitation', 'возбуждение'),
        ('appetence', 'влечение'),
        ('indifference', 'безразличие'),
        ('passion', 'страсть'),
    )

    situations = models.ManyToManyField(Situation, through='Connection', through_fields=('id_emotion', 'id_situation'), related_name='emotions', verbose_name = 'список ситуаций')
    emotion = models.CharField(max_length=16, choices=EMOTIONS, verbose_name = 'эмоция')

    
    def __str__(self):
        return self.emotion
    
    class Meta:
        verbose_name_plural = 'эмоции'
        verbose_name = 'эмоция'


class Connection(models.Model):
    id_situation = models.ForeignKey(Situation, on_delete=models.CASCADE, verbose_name = 'id ситуации')
    id_emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE, verbose_name = 'id эмоции')

    class Meta:
        verbose_name_plural = 'связи эмоций и ситуаций'
        verbose_name = 'связь эмоции и ситуации'