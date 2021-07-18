from rest_framework import authentication
from rundowns.models import Rundown
from .serializers import RundownSerializer
from rest_framework import viewsets


class RundownViewSet(viewsets.ModelViewSet):
    serializer_class = RundownSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Rundown.objects.all()
