from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# genre of the movie
class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
 
class Movie(models.Model):
    movie_name =models.CharField(max_length=100)
    movie_description = models.TextField()
    movie_image = models.ImageField(upload_to='photos/')
    age = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    ''' this is a many to many field because a movie can be attributed
    to multiple genres '''

    def __str__(self):
        return self.movie_name