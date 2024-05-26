from django.contrib import admin
from galeria.models import Imagem

class ImagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'codinome', 'foto', 'publicada')
    search_fields = ('nome', 'codinome')
    list_filter = ('nome', 'codinome')
    list_editable = ('publicada',)
    ordering = ('nome', 'codinome')
    list_display_links = ('id', 'nome', 'codinome')
    list_per_page = 10

admin.site.register(Imagem, ImagemAdmin)
