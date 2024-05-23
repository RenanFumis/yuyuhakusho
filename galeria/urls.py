from django.urls import path
from galeria.views import index, personagem, herois

urlpatterns = [
    path('', index, name='index'),
    path('personagem/', personagem, name='personagem'),
    path('herois/', herois, name='herois')

]