
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    output = 'Hello, World!'
    context = {}
    return render(request, 'index.html', context)

