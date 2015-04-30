from django.db import models

class Message(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	message = models.TextField()
	urlprofile = models.TextField()
	name = models.TextField()
	
