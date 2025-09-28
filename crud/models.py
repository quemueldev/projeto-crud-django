from django.db import models

class cachorro(models.Model):
    nome = models.CharField()
    raca = models.CharField()