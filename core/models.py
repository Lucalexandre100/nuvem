from django.db import models


# Create your models here.
class Arquivo(models.Model):
    nome = models.CharField(max_length=50)
    arquivo = models.FileField(upload_to='repositorio_arquivo')

    def __str__(self):
        return self.nome
