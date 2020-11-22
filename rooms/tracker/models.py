from django.db import models

class Room(models.Model):
	name = models.CharField(max_length=256, db_index=True)
	jitsiRoom = models.CharField(max_length=256, db_index=True)

	def __str__(self):
		return self.name + " (" + self.jitsiRoom + ")"
