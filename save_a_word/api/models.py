from django.db import models
from django.contrib.auth.models import User
import jsonfield

class Language(models.Model):
	code = models.CharField(max_length=15) # unique
	name = models.CharField(max_length=50) # unique

	def __str__(self):
		return self.code


class Word(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	base_word = models.TextField()
	base_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="base_language")

	translated_word = jsonfield.JSONField()
	foreign_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="foreign_language")


	def __str__(self):
		return f'{self.base_word}'
