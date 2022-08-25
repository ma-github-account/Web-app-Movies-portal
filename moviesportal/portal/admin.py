from django.contrib import admin
from .models import Category, Movie

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

	list_display = ['title', 'slug','available',]
	list_filter = ['available']
	list_editable = ['available']
	prepopulated_fields = {'slug': ('title',)}



