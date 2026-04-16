from rest_framework import viewsets

from cinema.models import Actor, CinemaHall, Genre, Movie, MovieSession
from cinema.serializers import (
    ActorSerializer,
    CinemaHallSerializer,
    GenreSerializer,
    MovieDetailSerializer,
    MovieListSerializer,
    MovieSerializer,
    MovieSessionDetailSerializer,
    MovieSessionListSerializer,
    MovieSessionSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrive":
            return MovieDetailSerializer
        else:
            return MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list" or "retrive":
            self.queryset = Movie.objects.prefetch_related("genres", "actors")
        return queryset

    class MovieSessionviewSet(viewsets.ModelViewSet):
        queryset = MovieSession.objects.all()
        serializer_class = MovieSessionSerializer

        def get_serializer_class(self):
            if self.action == "list":
                return MovieSessionListSerializer
            if self.action == "retrive":
                return MovieSessionDetailSerializer
            else:
                return MovieSessionSerializer

        def get_queryset(self):
            queryset = self.queryset
            if self.action == "list" or "retrive":
                queryset = MovieSession.objects.select_related("movie", "cinema_hall")
            return queryset
