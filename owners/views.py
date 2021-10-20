import json
from django.http import JsonResponse
from django.views import View
from .models import Owner, Dog


class OwnerView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            Owner.objects.create(
                name=data["name"], email=data["email"], age=data["age"]
            )
        except KeyError:
            return JsonResponse({"MESSAGE": "IVALID_KEY"}, status=400)
        return JsonResponse({"MESSAGE": "CREATED"}, status=201)

    def get(self, request):
        result = [
            {
                "name": owner.name,
                "mail": owner.email,
                "age": owner.age,
                "my_dogs": [
                    {"name": dog.name, "age": dog.age} for dog in owner.dogs.all()
                ],
            }
            for owner in Owner.objects.all()
        ]
        return JsonResponse({"MESSAGE": result}, status=200)


class DogView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            Dog.objects.create(
                name=data["name"],
                age=data["age"],
                owner=Owner.objects.get(name=data["owner"]),
            )
        except KeyError:
            return JsonResponse({"MESSAGE": "IVALID_KEY"}, status=400)
        return JsonResponse({"MESSAGE": "CREATED"}, status=201)

    def get(self, request):
        result = [
            {
                "name": dog.name,
                "age": dog.age,
                "owner": dog.owner.name,
            }
            for dog in Dog.objects.all()
        ]
        return JsonResponse({"MESSAGE": result}, status=200)
