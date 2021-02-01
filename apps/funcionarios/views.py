#imports para reportLab
import io
from django.http import FileResponse
from django.views import View
from reportlab.pdfgen import canvas
#imports para xhtml2pdf
from django.template.loader import get_template
from xhtml2pdf import pisa
#Imports gerais
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from apps.funcionarios.models import Funcionario


from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here
class HelloApiView(APIView):
    """API View de Teste"""

    def get(self, request, format=None):
        """Retornar lista de caracteristicas da API View"""
        an_apiview = [
            'Testando linha 1',
            'Testando linha 2',
            'Testando linha 3',
            'Testando linha 4',
        ]

        return Response(
            {
                'message': 'Hello',
                'an_apiview': an_apiview
             }
        )


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        #return Funcionario.objects.all()
        return Funcionario.objects.filter(empresa = empresa_logada)

class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome','departamentos','imagem']

class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')

class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome','departamentos','imagem']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0][0].lower() + funcionario.nome.split(' ')[1].lower()
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()

        return super(FuncionarioCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('list_funcionarios')

def relatorio_funcionarios(request):

    response = HttpResponse(content_type='application/pdf')

    #Content-Disposition serve para quando clicar no link o arquivo seja baixado para a máquina.
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf'

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(220, 810, "Relatório de funcionários:")
    p.drawString(0, 800, "_"*150)

    funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa)

    str_ = 'Nome: %s  |  Horas extras: %.2f'

    p.drawString(20, 760, "Empresa: %s " % (request.user.funcionario.empresa.nome))

    y = 730

    for funcionario in funcionarios:
        p.drawString(20, y, str_ % (funcionario.nome, funcionario.total_horas_extras))
        y -= 25

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), response)

        if not pdf.err:
            response = HttpResponse(response.getvalue(),content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error rendering PDF", status=400)

class Pdf(View):

    def get(self, request):
        params = {
            'today': 'Variável today',
            'sales': 'Variável sales',
            'request': request,
        }
        return Render.render('funcionarios/relatorio.html', params, 'myfile')









