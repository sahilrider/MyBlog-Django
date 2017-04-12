import datetime
from django.db import models
from django.db.models import permalink
from django.utils import timezone
# Create your models here.
class Genre(models.Model):
	title=models.CharField(max_length=30)
	'''slug = models.SlugField(max_length=100, unique=True)'''
	def __str__(self):
		return self.title
	'''@permalink
	def get_absolute_url(self):
		return ('view_blog_category', None, { 'slug': self.slug })'''

class Article(models.Model):
	title=models.CharField(max_length=50)
	'''slug = models.SlugField(max_length=100, unique=True)'''
	body = models.TextField()
	body=models.TextField()
	posted=models.DateTimeField('date published')
	genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
	def __str__(self):
		return self.title
	'''@permalink
	def get_absolute_url(self):
		return ('view_blog_post', None, { 'slug': self.slug })'''

