from datetime import datetime

from django.db import models
from markupfield.fields import MarkupField
from phonenumber_field.modelfields import PhoneNumberField


class NameAble(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        abstract = True


class LocateAble(models.Model):
    phone = PhoneNumberField()
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
