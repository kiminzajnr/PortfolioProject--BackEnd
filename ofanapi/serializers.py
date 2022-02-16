from .models import Homes, Groups, Join_Group
from rest_framework import serializers


class HomesSerializer(serializers.HyperlinkedModelSerializer):
    """ serialize Homes models"""
    class Meta:
        """ Return a list of all fields in model Homes"""
        model = Homes
        fields = '__all__'


class GroupsSerializer(serializers.HyperlinkedModelSerializer):
    """ serialize Groups models"""
    class Meta:
        model = Groups
        fields = '__all__'


class Join_GroupSerializer(serializers.HyperlinkedModelSerializer):
    """ serialize Groups models"""
    class Meta:
        model = Join_Group
        fields = '__all__'
