
from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

def index(request):
    output = 'Hello, World!'
    return HttpResponse(output, content_type='text/plain')

def getRooms():
    return Room.objects.all()
