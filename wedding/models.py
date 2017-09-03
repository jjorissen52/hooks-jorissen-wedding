from datetime import datetime

from django.db import models
from djmoney.models.fields import MoneyField

from wedding.mixins import NameAble, LocateAble, ScheduleAble


class UploadedPhoto(NameAble, models.Model):
    photo = models.FileField(upload_to="uploaded_photos")


class Event(ScheduleAble, models.Model):
    couple = models.CharField(max_length=100, blank=False, null=False)
    date = models.DateField(default=datetime.now)
    venue = models.ForeignKey('wedding.Venue', null=True, blank=True)

    def __str__(self):
        return f'{self.couple} at {self.venue} on {self.date}'


class Venue(NameAble, LocateAble, models.Model):
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

    # moneys
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)

    # logistics
    allotted_hours = models.PositiveSmallIntegerField()
    capacity = models.PositiveSmallIntegerField()
    alcohol_situation = models.CharField(max_length=1, default=1, choices=ALCOHOL_OPTIONS)
    alcohol_pricing = models.TextField(default='')
    food_situation = models.CharField(max_length=1, default=1, choices=FOOD_OPTIONS)
    logistics_comments = models.TextField(default='')

    def __str__(self):
        return f'{self.name}'