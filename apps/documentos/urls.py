from django.urls import path
from .views import DocumentosList, DocumentoEdit, DocumentoDelete, \
    DocumentoCreate, upload, documentos_list, documento_upload, documento_delete,\
    DocumentosListView, DocumentoUploadView, FuncionarioDocumentoUploadView

urlpatterns = [
path('', DocumentosList.as_view(), name='list_documentos'),
path('editar/<int:pk>/', DocumentoEdit.as_view(), name='update_documento'),
path('deletar/<int:pk>/', DocumentoDelete.as_view(), name='delete_documento'),
path('criar/<int:funcionario_id>/', DocumentoCreate.as_view(), name='create_documento'),
path('upload/', upload, name='upload'),
path('documentos_list/', documentos_list, name='documentos_list'),
path('documento_upload/', documento_upload, name='documento_upload'),
path('documento_delete/<int:pk>/', documento_delete, name='documento_delete'),
path('documentos_cbv_list/', DocumentosListView.as_view(), name='documentos_cbv_list'),
path('documento_cbv_upload/', DocumentoUploadView.as_view(), name='documento_cbv_upload'),
path('funcionario_documento_cbv_upload/', FuncionarioDocumentoUploadView.as_view(), name='funcionario_documento_cbv_upload'),
]