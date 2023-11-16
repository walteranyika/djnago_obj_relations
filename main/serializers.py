from rest_framework import serializers

from main.models import Artist, Album, Song


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["name", "dob", "country"]


class AlbumSerializer(serializers.ModelSerializer):
    # artists = serializers.StringRelatedField(read_only=True, many=True)
    artists = ArtistSerializer(read_only=True, many=True)
    songs = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ["name", "year", "artists", "songs"]


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["title", "length", "album"]
