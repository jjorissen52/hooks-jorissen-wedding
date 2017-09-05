import sys
from django.conf import settings
from wedding.models import Event, BackgroundPhoto, Content


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
        background_photos[photo.page] = f'https://{settings.AWS_S3_CUSTOM_DOMAIN}/' \
                                        f'{settings.AWS_LOCATION}/{photo.picture.file}'
    return {"background_photos": background_photos}


def content(request):
    content_objs = Content.objects.published()
    contents = {}
    for content in content_objs:
        try:
            content.image = f'https://{settings.AWS_S3_CUSTOM_DOMAIN}/{settings.AWS_LOCATION}/{content.picture.file}'
        except ValueError:
            pass
        if content.page in contents.keys():
            contents[content.page].append(content)
        else:
            contents[content.page] = [content]
    return {"contents": contents}


def debug(request):
    return {"debug": settings.DEBUG}
