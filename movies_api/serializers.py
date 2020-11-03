from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.HyperlinkedModelSerializer):
  """Serializes a new movie model"""
  class Meta:
    model = Movie
    fields = ['id', 'movie_title', 'main_actors',
              'description', 'genre', 'rate']
