from django.shortcuts import render, get_object_or_404
from galeria.models import Imagem


def index(request):
    return render(request, 'galeria/index.html')

def personagem(request):
    return render(request, 'galeria/personagem.html')

def herois(request):
    # dados={
    #     2: {
    #         "nome": "Keiko Yukimura",
    #         "codinome": "A Namorada"
    #     },
    #     3: {
    #         "nome": "Kazuma Kuwabara",
    #         "codinome": "O Espadachim"
    #     },
        
    #     }
    fotos = Imagem.objects.all()
    return render(request, 'galeria/herois.html', {'personagem': fotos})
