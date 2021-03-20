from django.db import models


class TimeStampedModel(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True)
    updated_datetime = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True
        ordering = ("-created_datetime",)
