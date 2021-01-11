from django.urls import path, include
from .views import HoraExtraList, HoraExtraEdit, HoraExtraDelete, HoraExtraCreate, \
    FuncionarioHoraExtraEdit, UtilizouHoraExtra, RecuperouHoraExtra

urlpatterns = [
path('', HoraExtraList.as_view(), name='list_horasextras'),
path('editar/<int:pk>/', HoraExtraEdit.as_view(), name='update_horasextras'),
path('editar-funcionario/<int:pk>/', FuncionarioHoraExtraEdit.as_view(), name='update_funcionario_horasextras'),
path('utilizou-hora-extra/<int:pk>/', UtilizouHoraExtra.as_view(), name='utilizou_hora_extra'),
path('recuperou-hora-extra/<int:pk>/', RecuperouHoraExtra.as_view(), name='recuperou_hora_extra'),
path('deletar/<int:pk>/', HoraExtraDelete.as_view(), name='delete_horasextras'),
path('criar/', HoraExtraCreate.as_view(), name='create_horasextras'),
]