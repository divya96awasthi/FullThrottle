from rest_framework import serializers
from .models import *


# it will convert model instances to native to dictionary which can be used for json rendering


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
