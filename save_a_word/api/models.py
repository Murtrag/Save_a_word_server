from django.db import models
from django.contrib.auth.models import User
import jsonfield

class Language(models.Model):
	code = models.CharField(max_length=15)
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.code


class Word(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	language = models.ForeignKey(Language, on_delete=models.CASCADE)
	word = models.TextField()
	translation = jsonfield.JSONField()

	def __str__(self):
		return f'{self.word}'
