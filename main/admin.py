from django.contrib import admin

# Register your models here.
from main.models import Artist, Album, Song


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'dob', 'country']
    list_per_page = 25


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'year']
    list_per_page = 25


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'length', 'album']
    list_per_page = 25

# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
