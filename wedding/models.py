from datetime import datetime

from django.db import models
from djmoney.models.fields import MoneyField
from markupfield.fields import MarkupField

from wedding.managers import PublishedManager
from wedding.mixins import NameAble, LocateAble, ScheduleAble, PictureAble, DescribeAble, RankAble, \
    PublishAble


class BaseBackground(NameAble, PictureAble, RankAble):
    pass


class Page(NameAble, PictureAble, DescribeAble, models.Model):
    slug = models.CharField(max_length=100, unique=True, blank=True)
    header = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = self.slug.lower() if self.slug else '-'.join(self.name.lower().split(' '))
        return super(Page, self).save(*args, **kwargs)


class Event(ScheduleAble, models.Model):
    couple = models.CharField(max_length=100, blank=False, null=False)
    venue = models.ForeignKey('wedding.Venue', null=True, blank=True)

    def __str__(self):
        return f'{self.couple} at {self.venue} on {self.start}'


class Venue(NameAble, LocateAble, PictureAble, DescribeAble, RankAble, models.Model):
    ALCOHOL_OPTIONS = (
        ('0', 'Alcohol provider of choice'),
        ('1', 'Alcohol provided by venue'),
        ('2', 'No Alcohol')

    )
    FOOD_OPTIONS = (
        ('0', 'Must use provided catering'),
        ('1', 'Must choose from approved caterers'),
        ('2', 'Any caterer is fine')
    )

    display_description = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Content(NameAble, PictureAble, DescribeAble, RankAble, PublishAble, models.Model):
    header = models.CharField(max_length=100)
    page = models.ForeignKey('Page')
    objects = PublishedManager()

    def __str__(self):
        return f'{self.name}'




