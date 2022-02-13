from rest_framework import viewsets

from .serializers import HomesSerializer
from .models import Homes


class HomesViewSet(viewsets.ModelViewSet):
    """ viewset for Homes model"""
    serializer_class = HomesSerializer
    queryset = Homes.objects.all()
