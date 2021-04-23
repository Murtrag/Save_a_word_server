from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Word
        fields = ['owner','language', 'word', 'translation', 'id']
class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Language
        fields = ['code', 'name']
