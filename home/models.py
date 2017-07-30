from django.db import models
from django.contrib.auth.models import User 

class House(models.Model):
	name = models.CharField(max_length=60)
	words = models.CharField(max_length=60)
	description = models.TextField()
	img = models.ImageField(verbose_name= 'emblem' ,
		upload_to='houses_emblems/', 
		blank=True)

	def __str__(self):
		return self.name

class Person(models.Model):
	house = models.ForeignKey(House)
	user = models.OneToOneField(User)
	name = models.CharField(max_length=60)
	biography = models.TextField()
	aliwe = models.BooleanField(default=True)
	img = models.ImageField(verbose_name= 'emblem' ,
		upload_to='users_image/', 
		blank=True)
	
	def __str__(self):
		return self.name