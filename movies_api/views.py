from django.shortcuts import render
# import local data
from .models import Movie
from .serializers import MovieSerializer
# import viewsets
from rest_framework import viewsets


class MovieViewSet(viewsets.ModelViewSet):
  """Renders the Movie model instances"""
  queryset = Movie.objects.all().order_by('movie_title')
  serializer_class = MovieSerializer
