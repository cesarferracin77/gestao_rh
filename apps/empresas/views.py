from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa

# Create your views here.
class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return redirect('home')

    def get_success_url(self):
        return reverse_lazy('create_empresa')

class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']