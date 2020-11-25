
from django.shortcuts import render
from django.http import HttpResponse
from tracker.views import getRooms
from rooms import config

def index(request):
    context = {'rooms': getRooms(), 
        'jitsiApiLink': config.jitsiApiLink,
        'jitsiDomain': config.jitsiDomain,
    }
    return render(request, 'index.html', context)

