from django.db import models


class PublishedManager(models.Manager):

    def published(self):
        return super(PublishedManager, self).get_queryset().filter(is_published=True).order_by('-rank', 'pk')