from rest_framework import serializers
from .models import newmodel

class newmodelSerializer(serializers.ModelSerializer):

    class Meta:
        model = newmodel
        fields = '__all__'