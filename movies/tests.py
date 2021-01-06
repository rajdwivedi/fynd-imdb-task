import json

from django.urls  import reverse
from rest_framework.test import  APITestCase
from rest_framework import status

from models import Movie, Genre
from movies.api.serializer import GenreSerializer, MovieSerializer
