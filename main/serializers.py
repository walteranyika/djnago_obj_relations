from rest_framework import serializers

from main.models import Artist, Album, Song


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["name", "dob", "country"]


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["name", "year", "artists"]


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["title", "length", "album"]
