from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Movie

# Create your views here.


def index(req):
    # select * from movies_movie
    movies = Movie.objects.all()  # from this we get all the movies from db

    # it'll search in templates/ by default:
    return render(req, 'movies/index.html', {'movies': movies})


def detail(req, movie_id):
    # movie = Movie.objects.get(pk=movie_id)
    # (or)
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(req, 'movies/detail.html', {'movie': movie})
