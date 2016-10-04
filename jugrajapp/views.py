from django.shortcuts import render

# Create your views here.
from .models import newmodel

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import newmodelSerializer

class ExampleView(APIView):
    """
    A view that can accept POST requests with JSON content.
    """
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        addfield = newmodel(wholestring = request.data)
        addfield.save()
        return Response({'recieve': request.data})

    def get(self, request, format=None):

        x = newmodel.objects.all()
        serializers = newmodelSerializer(x, many= True)
        return Response(serializers.data)