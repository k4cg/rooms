from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=256, db_index=True)
    jitsiRoom = models.CharField(max_length=256, db_index=True)

    def __str__(self):
        return self.name + " (" + self.jitsiRoom + ")"

class User(models.Model):
    nick = models.CharField(max_length=256, db_index=True)
    inRoom = models.ForeignKey('Room', on_delete=models.SET_NULL, blank=True, null=True)
    lastSeen = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if self.inRoom:
            return self.nick + "(in " + self.inRoom.jitsiRoom + ")"
        else:
            return self.nick
