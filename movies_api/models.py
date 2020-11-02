from django.db import models

# Create your models here.

class Movie(models.Model):
  """Movie review database model"""
  movie_title = models.CharField(max_length=100)
  main_actors = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  rate = models.CharField(max_length=5)

  def __str__(self):
      return self.movie_title 
  
