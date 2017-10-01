from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from wedding.views import HomeTemplateView, ContactTemplateView, VenueTemplateView, FoodTemplateView, GiftsTemplateView, \
    index_view, page_view

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', admin.site.urls),
    # the names of the urls need to be capitalized; they are used in the page title
    # url(r'^home/$', HomeTemplateView.as_view(), name='Home'),
    url(r'^home/$', index_view, name='home'),
    url(r'^page/(?P<slug>\w{0,50})/$', page_view, name='page'),
    url(r'^$', lambda request: HttpResponseRedirect(reverse('home')), name='index'),
    url(r'^logout/$', lambda request: HttpResponseRedirect(reverse('admin:logout')), name='logout'),
    url(r'^login/$', lambda request: HttpResponseRedirect(reverse('admin:login')), name='login'),
    # url(r'^contact/$', ContactTemplateView.as_view(), name='Contact'),
    # url(r'^venue/$', VenueTemplateView.as_view(), name='Venue'),
    # url(r'^food/$', FoodTemplateView.as_view(), name='Food'),
    # url(r'^gifts/$', GiftsTemplateView.as_view(), name='Gifts'),
]

# handler404 = 'wedding.views.custom_404'