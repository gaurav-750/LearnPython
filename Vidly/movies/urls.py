from django.urls import path
from . import views

# * movies/   -> This is the root
# * movies/1

urlpatterns = [
    # * root (127.0.0.1:8000/movies)
    path('', views.index, name='movies_index'),
    path('<int:movie_id>', views.detail, name='movies_detail')
]
