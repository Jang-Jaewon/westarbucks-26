import json
from django.http import JsonResponse
from django.views import View
from .models import Actor, Movie


class ActorListView(View):
    def get(self, request):
        actors = Actor.objects.all()
        result = []
        for actor in actors:
            movies = actor.movie_set.all()
            movie_list = []
            for movie in movies:
                movie_data = {
                    "title": movie.title,
                    "release_date": movie.release_date,
                    "running_time": movie.running_time,
                }
                movie_list.append(movie_data)
            result.append(
                {
                    "first_name": actor.first_name,
                    "last_name": actor.last_name,
                    "date_of_birth": actor.date_of_birth,
                    "movies": movie_list,
                }
            )
        return JsonResponse({"MESSAGE": result}, status=200)


class MovieListView(View):
    def get(self, request):
        movies = Movie.objects.all()
        result = []
        for movie in movies:
            actors = movie.actor.all()
            actor_list = []
            for actor in actors:
                actor_data = {
                    "name": actor.first_name + actor.last_name,
                    "date_of_birth": actor.date_of_birth,
                }
                actor_list.append(actor_data)
            result.append(
                {
                    "title": movie.title,
                    "release_date": movie.release_date,
                    "running_time": movie.running_time,
                    "actors": actor_list,
                }
            )
        return JsonResponse({"MESSAGE": result}, status=200)
