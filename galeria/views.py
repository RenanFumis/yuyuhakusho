from django.shortcuts import render, get_object_or_404
from galeria.models import Imagem


def index(request):
    return render(request, 'galeria/index.html')

def herois(request):
    fotos = Imagem.objects.filter(publicada=True)
    return render(request, 'galeria/herois.html', {'fotos': fotos})

def imagem(request, foto_id):
    foto = get_object_or_404(Imagem, pk=foto_id)
    return render(request, 'galeria/personagem.html', {'foto': foto})

def buscar(request):
    fotos = Imagem.objects.filter(publicada=True)
    if 'buscar' in request.GET:
        termo = request.GET['buscar']
        if termo:
            fotos = fotos.filter(nome__icontains=termo)
    return render(request, 'galeria/buscar.html', {'fotos': fotos})
