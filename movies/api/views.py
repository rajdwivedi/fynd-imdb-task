from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

from movies.api.serializer import MovieSerializer, GenreSerializer
from movies.models import Movie, Genre


class MovieListView(generics.ListAPIView):
    """
    Movie List View
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('director', 'name', 'genre__name')


class MovieCreateView(generics.CreateAPIView):
    """
    Movie create View
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Movie update and delete View
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

