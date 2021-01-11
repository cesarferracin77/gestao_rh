from django.db import models
from django.urls import reverse_lazy

from apps.funcionarios.models import Funcionario

# Create your models here.
class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100, help_text='Motivo da hora extra')
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=5, decimal_places=2)
    utilizada = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse_lazy('list_horasextras')

    def __str__(self):
        return self.motivo