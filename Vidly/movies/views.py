from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.


def index(req):
    # select * from movies_movie
    movies = Movie.objects.all()  # from this we get all the movies from db
    print('movies:', movies)
    return render(req, 'movies/index.html', {'movies': movies})
