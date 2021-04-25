from api import models
from django.contrib import admin
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
	list_display  = ('pk', 'code', 'name',)

@admin.register(models.Word)
class WordAdmin(admin.ModelAdmin):
	list_display  = ('pk','owner', 'base_word', 'translated_word')


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
