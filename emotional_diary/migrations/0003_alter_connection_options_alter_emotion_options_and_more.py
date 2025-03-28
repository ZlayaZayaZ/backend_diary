# Generated by Django 5.1.7 on 2025-03-26 10:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emotional_diary', '0002_alter_emotion_unique_together_connection_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='connection',
            options={'verbose_name': 'связь эмоции и ситуации', 'verbose_name_plural': 'связи эмоций и ситуаций'},
        ),
        migrations.AlterModelOptions(
            name='emotion',
            options={'verbose_name': 'эмоция', 'verbose_name_plural': 'эмоции'},
        ),
        migrations.AlterModelOptions(
            name='situation',
            options={'verbose_name': 'ситуация', 'verbose_name_plural': 'ситуации'},
        ),
        migrations.AlterField(
            model_name='connection',
            name='id_emotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emotional_diary.emotion', verbose_name='id эмоции'),
        ),
        migrations.AlterField(
            model_name='connection',
            name='id_situation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emotional_diary.situation', verbose_name='id ситуации'),
        ),
        migrations.AlterField(
            model_name='emotion',
            name='emotion',
            field=models.CharField(choices=[(None, 'выберите эмоцию'), ('fear', 'страх'), ('apathy', 'апатия'), ('pain', 'боль'), ('negation', 'отрицание'), ('anger', 'гнев'), ('disappointment', 'разочарование'), ('sadness', 'печаль'), ('admiration', 'восхищение'), ('joy', 'радость'), ('happiness', 'счастье'), ('excitation', 'возбуждение'), ('appetence', 'влечение'), ('indifference', 'безразличие'), ('passion', 'страсть')], max_length=16, verbose_name='эмоция'),
        ),
        migrations.AlterField(
            model_name='emotion',
            name='situations',
            field=models.ManyToManyField(related_name='emotions', through='emotional_diary.Connection', to='emotional_diary.situation', verbose_name='список ситуаций'),
        ),
        migrations.AlterField(
            model_name='situation',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='дата ситуации'),
        ),
        migrations.AddConstraint(
            model_name='connection',
            constraint=models.UniqueConstraint(fields=('id_situation', 'id_emotion'), name='emotion_situation_constraint'),
        ),
    ]
