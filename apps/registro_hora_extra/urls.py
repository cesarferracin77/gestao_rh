from django.urls import path, include
from .views import HoraExtraList, HoraExtraEdit, HoraExtraDelete, HoraExtraCreate

urlpatterns = [
path('', HoraExtraList.as_view(), name='list_horasextras'),
path('editar/<int:pk>/', HoraExtraEdit.as_view(), name='update_horasextras'),
path('deletar/<int:pk>/', HoraExtraDelete.as_view(), name='delete_horasextras'),
path('criar/', HoraExtraCreate.as_view(), name='create_horasextras'),
]