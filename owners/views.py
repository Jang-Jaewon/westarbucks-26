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
