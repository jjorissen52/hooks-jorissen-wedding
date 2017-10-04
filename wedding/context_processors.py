from wedding.models import Event, Page, BaseBackground


def event(request):
    event, venue = None, None
    events = Event.objects.all().order_by('-pk')
    if events:
        event, venue = events[0], events[0].venue
        # venue.image = f'https://{settings.AWS_S3_CUSTOM_DOMAIN}/{settings.AWS_LOCATION}/{venue.picture.file}'
    return {"event": event, "venue": venue, "debug": False}


def base_background(request):
    base_background_ = BaseBackground.objects.all().order_by('-pk')
    if base_background_:
        base_background_ = base_background_[0]
    return {"base_background": base_background_}


def pages(request):
    return {"pages": Page.objects.all().order_by('rank')}
