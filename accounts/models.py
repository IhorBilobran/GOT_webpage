from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from home.models import House

class Profile(models.Model):
	house = models.ForeignKey(House, blank=True, null=True)
	user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
	img = models.ImageField(upload_to='users-photo/', blank=True, null=True)
	city = models.CharField(max_length=60, default=' ', blank=True)
	created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.user)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()

class Post(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	title = models.CharField(max_length=50)
	text = models.TextField(max_length=1000)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-created', )

	def __str__(self):
		return str(self.title)
