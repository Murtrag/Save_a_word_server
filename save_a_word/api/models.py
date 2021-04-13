from django.db import models
from django.contrib.auth.models import User

class Language(models.Model):
	code = models.CharField(max_length=15)
	name = models.CharField(max_length=50)


class Word(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	language = models.ForeignKey(Language, on_delete=models.CASCADE)
	word = models.TextField()
	# translation = models.ForeignKey()

