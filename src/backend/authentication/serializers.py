from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class is used for serializing user app that is written by default
    """
    class Meta:
        model = User
        fields = ('url', 'username', 'email')
