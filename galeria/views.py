from django.shortcuts import render


def index(request):
    return render(request, 'galeria/index.html')

def personagem(request):
    return render(request, 'galeria/personagem.html')
