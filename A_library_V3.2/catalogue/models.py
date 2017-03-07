from django.db import models
class Post(models.Model):
	CallNum=models.CharField(max_length=140)
	Barcode=models.CharField(max_length=140)
	Genre=models.CharField(max_length=140)
	Title=models.CharField(max_length=140)
	Author=models.CharField(max_length=140)
	Status=models.CharField(max_length=140)
	date=models.DateTimeField()
	hidden_date=models.DateTimeField(null=True , editable=False)
	member_Name =models.CharField(max_length=140, null=True, default='Nill')
	def __str__(self):
		return  self.Title +"_____"+self.CallNum
