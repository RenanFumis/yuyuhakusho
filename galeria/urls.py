from django.urls import path
from galeria.views import index, personagem, herois

urlpatterns = [
    path('', index, name='index'),
    path('herois/', herois, name='herois'),

    path('personagem/', personagem, name='personagem')

]