from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse_lazy

from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do funcionário')
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(
        Empresa, on_delete=models.PROTECT, null=True, blank=True)
    imagem = models.ImageField(upload_to='funcionarios/imagens', null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.imagem.delete()
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('list_funcionarios')

    @property
    def total_horas_extras(self):
        return self.registrohoraextra_set.filter(utilizada=False).aggregate(Sum('horas'))['horas__sum'] or 0


    def __str__(self):
        return self.nome
