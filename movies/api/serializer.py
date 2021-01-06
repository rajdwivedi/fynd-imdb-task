from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from movies.models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    #  serializer for Genre model

    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(WritableNestedModelSerializer):
    genre = GenreSerializer(many=True)
    #  serializer for Movie  model

    class Meta:
        model = Movie
        fields = ('popularity', 'director', 'imdb_score', 'name', 'genre')
