from django.db import models

class Post(models.Model):
	CallNum=models.CharField(max_length=140)
	Title=models.TextField()
	Author=models.TextField()
	date=models.DateTimeField()

	def __str__(self):
		return self.Title