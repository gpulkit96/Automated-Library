from django.db import models

class Member(models.Model):
	Name=models.CharField(max_length=140)
	RollNo=models.CharField(max_length=140)
	Dues=models.CharField(max_length=140)
	Status=models.CharField(max_length=140)
	date=models.DateTimeField()

	def __str__(self):
		return self.Name