
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    output = 'Hello, World!'
    return HttpResponse(output, content_type='text/plain')
