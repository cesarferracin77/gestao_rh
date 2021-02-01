from rest_framework import viewsets
from apps.funcionarios.api.serializers import FuncionarioSerializer
from apps.funcionarios.models import Funcionario
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class FuncionarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
