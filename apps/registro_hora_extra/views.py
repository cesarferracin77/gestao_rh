import csv
import json
import xlwt

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from apps.registro_hora_extra.forms import RegistroHoraExtraForm
from apps.registro_hora_extra.models import RegistroHoraExtra
# Create your views here.

class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa = empresa_logada, funcionario = self.request.user.funcionario)

class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    success_url = reverse_lazy('list_horasextras')

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user':self.request.user})
        return kwargs

class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = True
        registro_hora_extra.save()

        funcionario = self.request.user.funcionario

        response = json.dumps({'mensagem':'Requisição executada',
                               'horas': float(funcionario.total_horas_extras),
                               'utilizou': True})

        return HttpResponse(response, content_type='application/json')

class RecuperouHoraExtra(View):
    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = False
        registro_hora_extra.save()

        funcionario = self.request.user.funcionario

        response = json.dumps({'mensagem':'Requisição executada',
                               'horas': float(funcionario.total_horas_extras)})

        return HttpResponse(response, content_type='application/json')

class FuncionarioHoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(FuncionarioHoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_success_url(self):
        return reverse_lazy('update_funcionario', args=[self.object.funcionario.id])

class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_horasextras')

class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user':self.request.user})
        return kwargs

    def get_success_url(self):
        return reverse_lazy('list_horasextras')

class ExportarParaCSV(View):
    def get(self, request):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="horas_extras.csv"'

        registro_he = RegistroHoraExtra.objects.filter(utilizada=False)

        writer = csv.writer(response)
        writer.writerow(['Id', 'Motivo', 'Funcionário', 'Horas não utilizadas', 'Horas totais'])

        for registro in registro_he:
            writer.writerow([registro.id, registro.motivo, registro.funcionario,
                             registro.funcionario.total_horas_extras, registro.horas])

        return response

class ExportarParaExcel(View):
    def get(self, request):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="horas_extras.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Banco de Horas')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id', 'Motivo', 'Funcionário', 'Horas', 'Horas totais']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        registros = RegistroHoraExtra.objects.filter(utilizada=False, funcionario__empresa = self.request.user.funcionario.empresa)

        row_num = 1

        for registro in registros:
            ws.write(row_num, 0, registro.id, font_style)
            ws.write(row_num, 1, registro.motivo, font_style)
            ws.write(row_num, 2, registro.funcionario.nome, font_style)
            ws.write(row_num, 3, registro.horas, font_style)
            ws.write(row_num, 4, registro.funcionario.total_horas_extras, font_style)
            row_num += 1

        wb.save(response)
        return response