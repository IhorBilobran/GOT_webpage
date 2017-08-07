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
