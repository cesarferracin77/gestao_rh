from django.db import models
from apps.funcionarios.models import Funcionario
from django.shortcuts import reverse


# Create your models here.
class Documento(models.Model):
    descricao = models.CharField(max_length=100, help_text='Descrição do documento')
    dono = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos/pdfs')
    imagem = models.ImageField(upload_to='documentos/imagens', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('update_funcionario', args=[self.dono.id])

    def delete(self, *args, **kwargs):
        self.arquivo.delete()
        self.imagem.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.descricao