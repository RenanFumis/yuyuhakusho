from django.contrib import admin
from galeria.models import Imagem

class ImagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'codinome', 'foto')
    search_fields = ('nome', 'codinome')
    list_filter = ('nome', 'codinome')
    ordering = ('nome', 'codinome')
    list_display_links = ('id', 'nome', 'codinome')

admin.site.register(Imagem, ImagemAdmin)
