import json

from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class WordSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.CharField(required=False)
    class Meta:
        model = models.Word
        fields = ['owner','language', 'word', 'translation', 'id']

    def create(self, validated_data):
        try:
            validated_data['translation'] = json.loads(validated_data['translation'])
        except (json.decoder.JSONDecodeError, KeyError):
            raise serializers.ValidationError({'translation':['The field Translation must be a json type']})
        return models.Word.objects.create(**validated_data)

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Language
        fields = ['code', 'name']
