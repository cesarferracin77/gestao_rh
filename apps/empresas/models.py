from django.db import models

# Create your models here.
from django.urls import reverse_lazy


class Empresa(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da empresa')

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse_lazy('home')