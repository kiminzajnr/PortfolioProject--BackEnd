from .models import Homes
from rest_framework import serializers


class HomesSerializer(serializers.HyperlinkedModelSerializer):
    """ serialize Homes models"""
    class Meta:
        """ Return a list of all fields in model Homes"""
        model = Homes
        fields = '__all__'