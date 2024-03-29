from django.db import models
from datetime import datetime

# Create your models here.
class Fotografia(models.Model):

    CATEGORIAS = [("NEBULOSA","Nebulosa"), ("ESTRELA","Estrela"), ("GALÁXIA","Galáxia"), ("PLANETA","Planeta")]

    nome = models.CharField(max_length=100, null=True, blank=False);
    legenda = models.CharField(max_length=150, null=False, blank=False);
    categoria = models.CharField(max_length=100, choices=CATEGORIAS, default='');
    descricao = models.TextField(null=False, blank=False);
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True);
    publicada = models.BooleanField(default=False);
    createdAt = models.DateTimeField(default=datetime.now, blank=False)
    

    def __str__(self):
        return self.nome