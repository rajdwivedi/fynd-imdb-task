from django.db import models


class Genre(models.Model):
    """
    Genre model
    """
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    """
    Movie model
    """
    popularity = models.FloatField()
    director = models.CharField(max_length=200, db_index=True)
    imdb_score = models.FloatField()
    name = models.CharField(max_length=200, db_index=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name