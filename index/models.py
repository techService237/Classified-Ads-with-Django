from django.db import models

 
class Ad(models.Model):
	title=models.fields.CharField(max_length=100)
	description=models.fields.TextField(max_length=5000)
	price=models.fields.FloatField()
	owner=models.fields.CharField(max_length=20)
	
