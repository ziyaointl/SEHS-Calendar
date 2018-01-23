from django.db import models

# Event model
class Event(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now = True)
    event_date = models.DateTimeField()
