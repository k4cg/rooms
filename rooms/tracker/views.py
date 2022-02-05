
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import ensure_csrf_cookie
from json import loads
from datetime import datetime, timedelta
import pytz

from .models import Room, User
from rooms import config

def index(request):
    output = 'Hello, World!'
    return HttpResponse(output, content_type='text/plain')

def getRooms():
    return Room.objects.all().order_by('-orderPrio','name')

def getOrCreateUser(nick):
    qs = User.objects.filter(nick=nick)
    if len(qs) > 0:
        u = qs[0]
    else:
        u = User()
        u.nick = nick
    return u

@ensure_csrf_cookie
def ping(request):
    if request.method == 'POST':
        reqData = loads(request.body)
        nick = reqData['nick']
        room = reqData['room']
        users = reqData['users']
        
        if nick:
            u = getOrCreateUser(nick)
            u.external = False
            u.inRoom = Room.objects.filter(jitsiRoom=room)[0]
            u.save()
    
        uList = {}
        rooms = getRooms()
        for r in rooms:
            qs = User.objects.filter(inRoom=r, lastSeen__gte=timezone.now()-timedelta(seconds=30))
            r.users = qs

            if r == u.inRoom:
                v = list(qs.values_list("nick", flat=True))
                for ui in users:
                    u = getOrCreateUser(ui)
                    if (ui not in v) or u.external:
                        u.inRoom = r
                        u.external = True
                        u.save()
        vnum = len( User.objects.filter(lastSeen__gte=timezone.now()-timedelta(hours=12)) )
        data = {'rooms': render(request, 'userlist.html', {'rooms': rooms, 'vnum': vnum, 'ack': config.acknowledgement}).content.decode() }
        return JsonResponse(data)

    return HttpResponse("request requires correct post", content_type='text/plain')

def getusersj(request=None):
    rooms = getRooms()
    j = {}
    for r in rooms:
        qs = User.objects.filter(inRoom=r, lastSeen__gte=timezone.now()-timedelta(seconds=30))
        ulist = []
        for u in qs:
            ulist.append( u.nick + (" (E)" if u.external else "") )
        j[r.name] = ulist
    if request is not None:
        return JsonResponse(j)
    else:
        return j

def getusers(request):
    j = getusersj()
    s = ""
    for r in j:
        s += "[%s]\n" % r
        for u in j[r]:
            s += u + "\n"
        s += "\n"
    return HttpResponse(s, content_type='text/plain')
