from django.urls import path
from . import views

# * movies/   -> This is the root
# movies/1/details

urlpatterns = [
    path('', views.index, name='index'),  # * root (127.0.0.1:8000/movies)
]
