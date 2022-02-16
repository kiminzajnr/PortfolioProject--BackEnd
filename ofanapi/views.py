from rest_framework import viewsets

from .serializers import (
    HomesSerializer,
    GroupsSerializer,
    Join_GroupSerializer
)
from .models import Homes, Groups, Join_Group


class HomesViewSet(viewsets.ModelViewSet):
    """ viewset for Homes model"""
    serializer_class = HomesSerializer
    queryset = Homes.objects.all()


class GroupsViewSet(viewsets.ModelViewSet):
    """ viewset for Groups model"""
    serializer_class = GroupsSerializer
    queryset = Groups.objects.all()


class Join_GroupViewSet(viewsets.ModelViewSet):
    """ viewset for Join_Group model"""
    serializer_class = Join_GroupSerializer
    queryset = Join_Group.objects.all()
