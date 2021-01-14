from apps.funcionarios.models import Funcionario
from rest_framework import serializers
from apps.registro_hora_extra.api.serializers import RegistroHoraExtraSerializer


class FuncionarioSerializer(serializers.ModelSerializer):

    registrohoraextra_set = RegistroHoraExtraSerializer(many=True)
    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'departamentos', 'empresa', 'user', 'imagem', 'total_horas_extras', 'registrohoraextra_set']
