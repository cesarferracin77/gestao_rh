from django.shortcuts import render
from django.urls import reverse_lazy

from apps.departamentos.models import Departamento
from django.views.generic import ListView, UpdateView, DeleteView, CreateView


# Create your views here.
class DepartamentosList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa = empresa_logada)

class DepartamentoEdit(UpdateView):
    model = Departamento
    fields = ['nome']

class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')

class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()

        return super(DepartamentoCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('list_departamentos')