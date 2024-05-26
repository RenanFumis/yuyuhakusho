from django.shortcuts import render, get_object_or_404
from galeria.models import Imagem


def index(request):
    return render(request, 'galeria/index.html')


def herois(request):
    fotos = Imagem.objects.all()
    return render(request, 'galeria/herois.html', {'fotos': fotos})

def imagem(request, foto_id):
    foto = get_object_or_404(Imagem, pk=foto_id)
    return render(request, 'galeria/personagem.html', {'foto': foto})

