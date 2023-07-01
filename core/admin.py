from django.contrib import admin
from core import models

@admin.register(models.Atores)
class AtoresAdmin(admin.ModelAdmin):
    list_display = 'primeiro_nome', 'segundo_nome', 'idade', \
                   'personalidade', 'show', 'imagem', 'link_videos',

@admin.register(models.Personalidade)
class PersonalidadeAdmin(admin.ModelAdmin):
    list_display = 'nome',

