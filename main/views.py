from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import Artist, Album
from main.serializers import ArtistSerializer, AlbumSerializer


def show(request):
    # artist = Artist.objects.order_by("?").first()
    # print("Artist is ", artist)
    # albums = artist.album_set.all()
    # print("---------Albums-----------")
    # for alb in albums:
    #     print(alb)
    #     # songs = alb.songs.all().values_list('title', flat=True)
    #     songs = alb.songs.all().values('title')
    #     print(songs)
    #     print("------Songs-------")
    #     for s in songs:
    #         print(s)

    # song = Song.objects.order_by("?").first()
    # print(song)
    # album = song.album
    # print(album)
    # artists = album.artists.all()
    # print(artists)
    # for a in artists:
    #     print(a.name, a.country, a.dob)

    # relationships in django

    album = Album.objects.first()
    # song = Song(title="Mado ya Sango", length=3.00, album=album)
    # song.save()

    artist = Artist.objects.filter(name__icontains='Madilu').first()

    return render(request, 'index.html')


@api_view(["GET", "POST"])
def api_artists(request):
    if request.method == "GET":
        artists = Artist.objects.all()
        serializer = ArtistSerializer(instance=artists, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):  # complain if something is amiss
            serializer.save()
            return Response({"message": "Artists added", "details": serializer.data})
        return Response({"error": "invalid data"})


@api_view(["GET"])
def api_single_artist(request, pk):
    try:
        artist = Artist.objects.get(pk=pk)
        serializer = ArtistSerializer(instance=artist)
        return Response(serializer.data)
    except:
        return Response({"error": "Does not exist"}, status=404)


@api_view(["DELETE"])
def api_delete_artist(request, pk):
    try:
        artist = Artist.objects.get(pk=pk)
        artist.delete()
        return Response({"success": "Deleted"})
    except:
        return Response({"error": "Does not exist"}, status=404)


@api_view(["PUT", "PATCH"])
def api_update_artist(request, pk):
    try:
        artist = Artist.objects.get(pk=pk)
        serializer = ArtistSerializer(instance=artist, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"success": "Updated"})
    except:
        return Response({"error": "Does not exist"}, status=404)


@api_view(["GET"])
def api_albums_artist(request, pk):
    try:
        artist = Artist.objects.get(pk=pk)
        albums = artist.album_set.all()
        serializer = AlbumSerializer(instance=albums, many=True)
        return Response(serializer.data)
    except:
        return Response({"error": "Does not exist"}, status=404)
