from django.shortcuts import render
from .models import Event

def index(request):
    all_events = Event.objects.all()
    next_two_events = Event.objects.order_by('-event_date')[:2]
    return render(request, 'main/index.html', {
        'next_two_events': next_two_events
    })