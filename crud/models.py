from django.db import models

class cachorro(models.Model):
    nome = models.CharField(max_length=12)
    raca = models.CharField(max_length=10)