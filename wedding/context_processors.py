import sys
from django.conf import settings
from wedding.models import Event, BackgroundPhoto


def event(request):
    event, venue = None, None
    events = Event.objects.all().order_by('-pk')
    if events:
        event, venue = events[0], events[0].venue
    return {"event": event, "venue": venue, "debug": settings.DEBUG}


def backgrounds(request):
    background_photo_objs = BackgroundPhoto.objects.all()
    background_photos = {}
    for photo in background_photo_objs:
        print(settings.AWS_S3_CUSTOM_DOMAIN)
        background_photos[photo.page] = f'https://{settings.AWS_S3_CUSTOM_DOMAIN}/' \
                                        f'{settings.AWS_LOCATION}/{photo.picture.file}'
        print(background_photos)
    return {"background_photos": background_photos}


def debug(request):
    return {"debug": settings.DEBUG}
