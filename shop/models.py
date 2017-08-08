from django.db import models
from django.core.validators import MinValueValidator

from home.models import House

class Category(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True, null=True)
	img = models.ImageField(upload_to='default_pic',blank=True, null=True)

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name

class Product(models.Model):
	reference = models.ForeignKey(House, blank=True, null=True)
	category = models.ForeignKey(Category)

	name = models.CharField(max_length=50)
	description = models.TextField(blank=True)
	img = models.ImageField(upload_to='goods/%Y/%m/%d', blank=True, null=True)
	available = models.BooleanField(default=True)
	price = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)])
	created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated = models.DateTimeField(auto_now=True, null=True, blank=True)

	def __str__(self):
		return self.name
