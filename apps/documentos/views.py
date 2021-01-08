from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from apps.documentos.models import Documento
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.core.files.storage import FileSystemStorage

from apps.documentos.forms import DocumentoForm




# Create your views here.
from apps.funcionarios.models import Funcionario


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('documento')
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'documentos/upload.html')

def documentos_list(request):
    documentos = Documento.objects.all()
    return render(request, 'documentos/documentos_list.html', {
        'documentos': documentos
    })


def documento_upload(request, funcionario_id):
    if request.method=='POST':
        form = DocumentoForm(request.POST, request.FILES)
        form.instance.dono_id = funcionario_id
        if form.is_valid():
            form.save()
            return redirect('documentos_list')
    else:
        form = DocumentoForm()
    return render(request, 'documentos/documento_upload.html',{
        'form': form
    })

def documento_delete(request, pk):
    if request.method=='POST':
        documento = Documento.objects.get(pk=pk)
        documento.delete()
    return redirect('documentos_list')

class DocumentosList(ListView):
    model = Documento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Documento.objects.filter(empresa = empresa_logada)

class DocumentoEdit(UpdateView):
    model = Documento
    fields = ['descricao','arquivo']

class DocumentoDelete(DeleteView):
    model = Documento
    success_url = reverse_lazy('list_documentos')


class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'dono', 'arquivo']
   # success_url = reverse_lazy('list_funcionarios')

    def get_object(self, queryset=None):
        dono_id = self.kwargs.get("funcionario_id")
        return Funcionario.objects.get(user_id=dono_id)

    def post(self, request, *args, **kwargs):
        func_id = self.kwargs.get("funcionario_id")
        form = self.get_form()
        form.instance.dono_id = func_id

        uploaded_file = request.FILES.get('arquivo')
       # print(uploaded_file.name)
      #  print(uploaded_file.size)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def get_success_url(self):
        return reverse_lazy('list_funcionarios')

class DocumentosListView(ListView):
    model = Documento
    template_name = 'documentos/class_documentos_list.html'
    context_object_name = 'documentos'

    def get_queryset(self):
        funcionario = self.request.user.funcionario
        return Documento.objects.filter(dono = funcionario)

    def get_absolute_url(self):
        return reverse_lazy('documentos_cbv_list', kwargs={"funcionario_id":self.kwargs.get("funcionario_id")})

class DocumentoUploadView(CreateView):
    model = Documento
    #form_class = DocumentoForm
    fields = ['descricao', 'arquivo', 'imagem']
    template_name = 'documentos/documento_upload.html'

    def post(self, request, *args, **kwargs):
        #func_id = self.kwargs.get("funcionario_id")
        dono = self.request.user.funcionario
        form = self.get_form()
        form.instance.dono_id = dono.id

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_absolute_url(self):
        return reverse_lazy('documento_cbv_upload')

class FuncionarioDocumentoUploadView(CreateView):
    model = Documento
    #form_class = DocumentoForm
    fields = ['descricao', 'arquivo', 'imagem']
    template_name = 'documentos/documento_upload.html'

    def post(self, request, *args, **kwargs):
        #func_id = self.kwargs.get("funcionario_id")
        dono = self.request.user.funcionario
        form = self.get_form()
        form.instance.dono_id = dono.id

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_absolute_url(self):
        return reverse_lazy('documento_cbv_upload')

    def get_success_url(self):
        return reverse_lazy('update_funcionario', args=[self.object.dono.id])