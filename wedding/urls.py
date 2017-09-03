from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from wedding.views import HomeTemplateView, ContactTemplateView

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', HomeTemplateView.as_view(), name='home'),
    url(r'^$', lambda request: HttpResponseRedirect(reverse('home')), name='index'),
    url(r'^contact/$', ContactTemplateView.as_view(), name='contact'),
]
