from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from django.contrib.auth.models import User
from . import serializers
from . import models

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer



class WordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows word to be viewed or edited.
    """
    queryset = models.Word.objects.all().order_by('id')
    serializer_class = serializers.WordSerializer
    # permission_classes = [permissions.IsAuthenticated]

class LanguageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows language to be viewed or edited.
    """
    queryset = models.Language.objects.all().order_by('id')
    serializer_class = serializers.LanguageSerializer
    # permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'head']
