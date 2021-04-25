from django.contrib import admin
from api import models


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
	list_display  = ('pk', 'code', 'name',)

@admin.register(models.Word)
class WordAdmin(admin.ModelAdmin):
	list_display  = ('pk','owner', 'base_word', 'translated_word')
