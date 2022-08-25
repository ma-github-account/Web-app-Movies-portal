from django.shortcuts import render, get_object_or_404
from .models import Category, Movie

def movie_list(request, category_slug=None):

	category = None
	categories = Category.objects.all()
	movies = Movie.objects.filter(available=True)

	if category_slug:
	
		category = get_object_or_404(Category, slug=category_slug)
		movies = movies.filter(category=category)

	return render(request, 'portal/movie/list.html', {'category': category, 'categories': categories, 'movies': movies})


def movie_detail(request, id, slug):

	movie = get_object_or_404(Movie, id=id, slug=slug, available=True)

	return render(request, 'portal/movie/detail.html', {'movie': movie})