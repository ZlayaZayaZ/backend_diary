from django.contrib import admin

# Register your models here.
from .models import Situation, Emotion, Connection

class SituationAdmin(admin.ModelAdmin):
    list_display = ('rating_of_the_situation', 'description', 'conclusions', 'body_reaction', 'created_at',)
    list_display_links = ('description', 'conclusions',)
    search_fields = ('description', 'conclusions',)

class EmotionAdmin(admin.ModelAdmin):
    list_display = ('emotion', )

class ConnectionAdmin(admin.ModelAdmin):
    list_display = ('id_situation', 'id_emotion')
    list_display_links = ('id_situation', 'id_emotion')

admin.site.register(Situation, SituationAdmin)
admin.site.register(Emotion, EmotionAdmin)
admin.site.register(Connection, ConnectionAdmin)
