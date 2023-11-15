from django.shortcuts import render

# Create your views here.
from main.models import Artist, Song


def show(request):
    artist = Artist.objects.order_by("?").first()
    print("Artist is ", artist)
    albums = artist.album_set.all()
    print("---------Albums-----------")
    for alb in albums:
        print(alb)
        songs = alb.songs.all()
        print("------Songs-------")
        for s in songs:
            print(s)

    # song = Song.objects.order_by("?").first()
    # print(song)
    # album = song.album
    # print(album)
    # artists = album.artists.all()
    # print(artists)
    # for a in artists:
    #     print(a.name, a.country, a.dob)

    # relationships in django
    return render(request, 'index.html')
