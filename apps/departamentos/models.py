from django.db import models

# Create your models here.
class Departamento(models.Model):
    nome = models.CharField(max_length=70, help_text='Nome do departamento')

    def __str__(self):
        return self.nome