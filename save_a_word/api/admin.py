from django.contrib import admin
from api import models

@admin.register(models.Word)
class LanguageAdmin(admin.ModelAdmin):
	list_display  = ('pk','owner', 'language', 'word',)

@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
	list_display  = ('pk', 'code', 'name',)
