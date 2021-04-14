from django.contrib import admin
from api import models

# Register your models here.
admin.site.register(models.Word)

# admin.site.register(models.Language)
@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
	list_display  = ('pk', 'code', 'name',)
