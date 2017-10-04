from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from wedding.models import Page, Content


def index_view(request):
    pages = Page.objects.all().order_by('rank')
    # for page in pages:
    #     page.image = f'https://{settings.AWS_S3_CUSTOM_DOMAIN}/{settings.AWS_LOCATION}/{venue.picture.file}'
    return render(request, template_name='index.html', context={"pages": pages})


def page_view(request, slug):
    try:
        page = Page.objects.get(slug=slug).order_by('rank')
        contents = Content.objects.filter(page=page).order_by('rank')
        if not contents:
            raise Http404
    except Page.DoesNotExist:
        raise Http404

    return render(request, template_name='content.html', context={"contents": contents})


class HomeTemplateView(TemplateView):
    template_name = "index.html"


class ContactTemplateView(TemplateView):
    template_name = "contact.html"


class VenueTemplateView(TemplateView):
    template_name = "venue.html"


class FoodTemplateView(TemplateView):
    template_name = "food.html"


class GiftsTemplateView(TemplateView):
    template_name = "gifts.html"