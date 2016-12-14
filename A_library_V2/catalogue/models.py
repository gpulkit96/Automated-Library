from django.db import models

class Post(models.Model):
	CallNum=models.CharField(max_length=140)
	Genre=models.CharField(max_length=140)
	Title=models.CharField(max_length=140)
	Author=models.CharField(max_length=140)
	Status=models.CharField(max_length=140)
	date=models.DateTimeField()

	def __str__(self):
		return self.Title

class Member(models.Model):
	Name=models.CharField(max_length=140)
	RollNo=models.CharField(max_length=140)
	Dues=models.CharField(max_length=140)
	Status=models.CharField(max_length=140)
	date=models.DateTimeField()

	def __str__(self):
		return self.Name