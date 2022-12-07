from django.contrib import admin
from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    # * changing the default presentation of the Object in 'Admin panel'
    # so 'id' and 'name' will be displayed
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('title', 'number_in_stock', 'daily_rate')


# * Register your models here which you want to manage using Admin panel:
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
