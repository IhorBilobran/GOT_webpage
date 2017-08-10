from django.db import models
from django.contrib.auth.models import User

from home.models import House

class UserProfile(models.Model):
	house = models.ForeignKey(House, blank=True, null=True)
	user = models.OneToOneField(User, blank=True, null=True)
	img = models.ImageField(upload_to='users-photo/', blank=True, null=True)
	city = models.CharField(max_length=60, default=' ')
	created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.user)

class Post(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	title = models.CharField(max_length=50)
	text = models.TextField(max_length=1000)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('created', )
