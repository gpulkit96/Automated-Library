from django.db import models

class Member(models.Model):
	Name=models.CharField(max_length=140)
	RollNo=models.TextField()
	Dues=models.TextField()
	date=models.DateTimeField()

	def __str__(self):
		return self.Name