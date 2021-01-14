from rest_framework import viewsets
from apps.registro_hora_extra.api.serializers import RegistroHoraExtraSerializer
from apps.registro_hora_extra.models import RegistroHoraExtra


class RegistroHoraExtraViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RegistroHoraExtra.objects.all()
    serializer_class = RegistroHoraExtraSerializer
