from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from wedding.models import Event, Venue, Page, Content, BaseBackground

admin.site.unregister(User)


def make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)
make_published.short_description = "Publish Selected"


def unmake_published(modeladmin, request, queryset):
    queryset.update(is_published=False)
unmake_published.short_description = "Un-Publish Selected"

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
    _excluded_fields = ['event', '_address_rendered', '_description_rendered', 'description']
    _fields = {field.name for field in Model._meta.get_fields()} - {*_excluded_fields}
    # list_display = list(filter(lambda x, _fields=_fields: x in _fields, _ordered_fields))
    list_display = ['id', 'name', 'phone', 'picture', 'display_description']
    list_display_links = ['id']
    _fields -= {*list_display_links}
    # list_editable = list(filter(lambda x, _fields=_fields: x in _fields, _ordered_fields))


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    Model = Page
    _ordered_fields = [field.name for field in Model._meta.get_fields()]
    _excluded_fields = ['_description_rendered', 'content']
    _fields = {field.name for field in Model._meta.get_fields()} - {*_excluded_fields}
    list_display = list(filter(lambda x, _fields=_fields: x in _fields, _ordered_fields))
    list_display_links = ['id']
    _fields -= {*list_display_links}
    list_editable = list(filter(lambda x, _fields=_fields: x in _fields, _ordered_fields))


@admin.register(BaseBackground)
class BaseBackground(admin.ModelAdmin):
    Model = BaseBackground
    _ordered_fields = [field.name for field in Model._meta.get_fields()]
    _excluded_fields = ['_description_rendered', 'content']
    _fields = {field.name for field in Model._meta.get_fields()} - {*_excluded_fields}
    list_display = list(filter(lambda x, _fields=_fields: x in _fields, _ordered_fields))
    list_display_links = ['id']
    _fields -= {*list_display_links}
    list_editable = list(filter(lambda x, _fields=_fields: x in _fields, _ordered_fields))


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    Model = Content
    _ordered_fields = [field.name for field in Model._meta.get_fields()]
    _excluded_fields = ['_description_rendered', 'description', ]
    _fields = {field.name for field in Model._meta.get_fields()} - {*_excluded_fields}
    list_display = list(filter(lambda x, _fields=_fields: x in _fields, _ordered_fields))
    list_display_links = ['id', 'name']
    _fields -= {*list_display_links}
    list_editable = list(filter(lambda x, _fields=_fields: x in _fields, _ordered_fields))
    list_filter = ['page', 'rank']
    actions = [make_published, unmake_published]