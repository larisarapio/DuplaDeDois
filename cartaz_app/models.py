from django.db import models
from datetime import datetime

class Cartaz(models.Model):
    titulo = models.CharField(max_length=100, blank = False)
    subtitulo = models.CharField(max_length=100, null=True)
    horario1 = models.TimeField(auto_now=False, null=True)
    horario2 = models.TimeField(auto_now=False, null=True)
    data_lancamento = models.DateField(default=datetime.now)
    sinopse = models.TextField(max_length=400)
    link_trailer = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='imagens/%Y/%m/%d')
    em_cartaz = models.BooleanField(default=False)
    

    def __str__(self):
        return self.titulo
