from django.db import models
from datetime import timedelta

# Event model
class Event(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    all_day = models.BooleanField('All Day Event', default = False)
    last_modified = models.DateTimeField(auto_now = True)
    date = models.DateTimeField()
    duration = models.DurationField(default = timedelta(hours = 1))
    
    def get_title(self):
        return self.title
        
    def get_month(self):
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        return months[self.date.month - 1]

    def get_start_time(self):
        start_hour = str(self.date.hour)
        start_minute = '{:02d}'.format(self.date.minute)
        return start_hour + ':' + start_minute
        
    def get_finish_time(self):
        finish_date = self.date + self.duration
        finish_hour = str(finish_date.hour)
        finish_minute = '{:02d}'.format(finish_date.minute)
        return finish_hour + ':' + finish_minute