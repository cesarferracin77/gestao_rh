from django.db import models

# Create your models here.
class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100, help_text='Motivo da hora extra')

    def __str__(self):
        return self.motivo