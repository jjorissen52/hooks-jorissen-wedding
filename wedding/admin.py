from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from wedding.models import Event, Venue

admin.site.unregister(User)


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    Model = Event
    _ordered_fields = [field.name for field in Model._meta.get_fields()]
    _excluded_fields = []
    _fields = {field.name for field in Model._meta.get_fields()} - {*_excluded_fields}
    list_display = list(filter(lambda x, _fields=_fields: x in _fields, _ordered_fields))
    list_display_links = ['id']
    _fields -= {*list_display_links}
    list_editable = list(filter(lambda x, _fields=_fields: x in _fields, _ordered_fields))


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    Model = Venue
    _ordered_fields = [field.name for field in Model._meta.get_fields()]
    _excluded_fields = ['event', '_address_rendered']
    _fields = {field.name for field in Model._meta.get_fields()} - {*_excluded_fields}
    list_display = list(filter(lambda x, _fields=_fields: x in _fields, _ordered_fields))
    list_display_links = ['id']
    _fields -= {*list_display_links}
    list_editable = list(filter(lambda x, _fields=_fields: x in _fields, _ordered_fields))