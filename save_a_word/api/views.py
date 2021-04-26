from . import models
from . import serializers
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class WordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows word to be viewed, edited or removed.
    """
    serializer_class = serializers.WordSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        try:
            return models.Word.objects.filter(owner=self.request.user)
        except TypeError:
            return models.Word.objects.none()

    def perform_create(self, serializer):
        instance = serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs): 
        try:
            instance = self.get_object()
            if instance.owner != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)

            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

class LanguageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows language to be viewed or edited.
    """
    queryset = models.Language.objects.all().order_by('id')
    serializer_class = serializers.LanguageSerializer
    http_method_names = ['get', 'head']


class ObtainAuthToken(ObtainAuthToken):
    """
    API endpoint that provides a way to obtain user token.
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
