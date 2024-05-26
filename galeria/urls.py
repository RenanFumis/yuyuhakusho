from django.urls import path
from galeria.views import index, imagem, herois

urlpatterns = [
    path('', index, name='index'),
    path('herois/', herois, name='herois'),

    path('imagem/<int:foto_id>', imagem, name='imagem')

]