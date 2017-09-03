from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = "index.html"


class ContactTemplateView(TemplateView):
    template_name = "contact.html"


class VenueTemplateView(TemplateView):
    template_name = "venue.html"