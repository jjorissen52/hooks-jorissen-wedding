from datetime import datetime

from django.db import models
from markupfield.fields import MarkupField
from phonenumber_field.modelfields import PhoneNumberField


class NameAble(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        abstract = True


class LocateAble(models.Model):
    phone = models.CharField(max_length=10, null=True, blank=True)
    address = MarkupField(default="No Address Provided")

    class Meta:
        abstract = True


class ScheduleAble(models.Model):
    start = models.DateTimeField(default=datetime.now)
    end = models.DateTimeField(default=datetime.now)

    class Meta:
        abstract = True


class PictureAble(models.Model):
    picture = models.FileField(upload_to="uploaded_photos", blank=True, null=True)

    class Meta:
        abstract = True


class DescribeAble(models.Model):
    description = MarkupField(default="No Description Provided", default_markup_type='markdown')

    class Meta:
        abstract = True


class AttachAble(models.Model):
    PAGE_CHOICES = (
        ('Home', 'Home'),
        ('Food', 'Food'),
        ('Contact', 'Contact'),
        ('Gifts', 'Gifts'),
        ('Venue', 'Venue'),
        ('RSVP', 'RSVP'),
    )
    page = models.CharField(default='Home', max_length=10, choices=PAGE_CHOICES)

    class Meta:
        abstract = True


class PublishAble(models.Model):
    is_published = models.BooleanField(default=True)

    class Meta:
        abstract = True


class RankAble(models.Model):
    rank = models.PositiveSmallIntegerField(help_text='Lower is better.')

    class Meta:
        abstract = True
