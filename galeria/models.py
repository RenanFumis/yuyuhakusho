from django.db import models

class Imagem(models.Model):
  nome = models.CharField(max_length=150, null=False, blank=False)
  codinome = models.CharField(max_length=200, null=False, blank=False)
  introducao_1 = models.TextField(null=False, blank=False)
  introducao_2 = models.TextField(null=False, blank=False)
  profissao = models.CharField(max_length=200, null=False, blank=False)
  text_profissao = models.TextField(null=False, blank=False)
  text_habilidades = models.TextField(null=False, blank=False)
  text_final_1 = models.TextField(null=False, blank=False)
  text_final_2 = models.TextField(null=False, blank=False)
  foto = models.CharField(max_length=150, null=False, blank=False)

  def __str__(self):
    return f"Imagem [nome={self.nome}]"