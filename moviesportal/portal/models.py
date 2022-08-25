from django.db import models
from django.urls import reverse

class Category(models.Model):

	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True, unique=True)

	class Meta:
		
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):

		return reverse('portal:movie_list_by_category', args=[self.slug])

class Movie(models.Model):

	category = models.ForeignKey(Category, related_name='movies', on_delete=models.CASCADE)
	title = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	image = models.ImageField(upload_to='movies/%Y/%m/%d', blank=True)
	year = models.DecimalField(max_digits=4, decimal_places=0)
	language = models.CharField(max_length=200, db_index=True)
	cast = models.TextField(blank=True)
	director = models.CharField(max_length=200, db_index=True)
	description = models.TextField(blank=True)
	plot = models.TextField(blank=True)
	available = models.BooleanField(default=True)

	class Meta:
		
		ordering = ('title',)
		index_together = (('id', 'slug'),)
	
	def __str__(self):
	
		return self.title
	
	def get_absolute_url(self):
	
		return reverse('portal:movie_detail', args=[self.id, self.slug])