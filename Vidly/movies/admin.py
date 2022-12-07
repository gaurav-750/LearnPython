from django.contrib import admin
from .models import Genre, Movie

# * Register your models here which you want to manage using Admin panel:
admin.site.register(Genre)
admin.site.register(Movie)
