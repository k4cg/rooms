
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from json import loads
from datetime import datetime, timedelta
import pytz

from .models import Room, User

def index(request):
    output = 'Hello, World!'
    return HttpResponse(output, content_type='text/plain')

def getRooms():
    return Room.objects.all()

def ping(request):
    if request.is_ajax() and request.method == 'POST':
        reqData = loads(request.body)
        nick = reqData['nick']
        room = reqData['room']
        
        if nick:
            qs = User.objects.filter(nick=nick)
            if len(qs) > 0:
                u = qs[0]
            else:
                u = User()
                u.nick = nick
            u.inRoom = Room.objects.filter(jitsiRoom=room)[0]
            u.save()
    
    uList = {}
    rooms = getRooms()
    for r in rooms:
        qs = User.objects.filter(inRoom=r, lastSeen__gte=timezone.now()-timedelta(seconds=60))
        uList[r.name] = [u.nick for u in qs]
    
    data = {'rooms': uList}
    return JsonResponse(data)
