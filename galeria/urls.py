from django.urls import path
from galeria.views import index, personagem

urlpatterns = [
    path('', index),
    path('personagem/', personagem)
]