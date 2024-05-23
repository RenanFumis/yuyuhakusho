from django.shortcuts import render


def index(request):
    return render(request, 'galeria/index.html')

def personagem(request):
    return render(request, 'galeria/personagem.html')

def herois(request):
    return render(request, 'galeria/herois.html')
