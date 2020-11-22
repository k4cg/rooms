
from django.shortcuts import render
from django.http import HttpResponse
from tracker.views import getRooms

def index(request):
    context = {'rooms': getRooms()}
    return render(request, 'index.html', context)

