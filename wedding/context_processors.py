import sys
from django.conf import settings
from wedding.models import Event


def event(request):
    event, venue = None, None
    events = Event.objects.all().order_by('-pk')
    if events:
        event, venue = events[0], events[0].venue
    return {"event": event, "venue": venue, "debug": settings.DEBUG}


def debug(request):
    return {"debug": settings.DEBUG}
