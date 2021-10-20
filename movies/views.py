import json
from django.http import JsonResponse
from django.views import View
from .models import Actor, Movie


class ActorListView(View):
    def get(self, request):
        result = [
            {
                "first_name": actor.first_name,
                "last_name": actor.last_name,
                "date_of_birth": actor.date_of_birth,
                "movies": [
                    {
                        "title": movie.title,
                        "release_date": movie.release_date,
                        "running_time": movie.running_time,
                    }
                    for movie in actor.movies.all()
                ],
            }
            for actor in Actor.objects.all()
        ]
        return JsonResponse({"MESSAGE": result}, status=200)


class MovieListView(View):
    def get(self, request):
        result = [
            {
                "title": movie.title,
                "release_date": movie.release_date,
                "running_time": movie.running_time,
                "actors": [
                    {
                        "name": actor.last_name + actor.first_name,
                        "date_of_birth": actor.date_of_birth,
                    }
                    for actor in movie.actor.all()
                ],
            }
            for movie in Movie.objects.all()
        ]
        return JsonResponse({"MESSAGE": result}, status=200)
