from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from core.models import CodeGenerated
from core.serializers import CodeGeneratedSerializer


class CodeGeneratedViewSet(viewsets.ModelViewSet):
    queryset = CodeGenerated.objects.all()
    serializer_class = CodeGeneratedSerializer