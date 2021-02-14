from django.shortcuts import render
#from django.http import HttpResponse
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Views below this
#def main(request):
#   return HttpResponse("<h1>first test</h1>")

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer