from django.shortcuts import render
from .models import Event

def index(request):
    all_events = Event.objects.all()
    next_two_events = Event.objects.order_by('date')[:2]
    return render(request, 'main/index.html', {
        'next_two_events': next_two_events
    })