from django.urls import path
from . import views

app_name = 'portal'
urlpatterns = [

	path('', views.movie_list, name='movie_list'),
	path('<slug:category_slug>/', views.movie_list, name='movie_list_by_category'),
	path('<int:id>/<slug:slug>/', views.movie_detail, name='movie_detail'),

]
