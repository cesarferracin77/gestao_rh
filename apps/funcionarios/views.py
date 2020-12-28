from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from apps.funcionarios.models import Funcionario


# Create your views here
class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        #return Funcionario.objects.all()
        return Funcionario.objects.filter(empresa = empresa_logada)

class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome','departamentos']

class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')

class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome','departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0][0].lower() + funcionario.nome.split(' ')[1].lower()
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()

        return super(FuncionarioCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('list_funcionarios')