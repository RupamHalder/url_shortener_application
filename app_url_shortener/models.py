import uuid
from datetime import datetime

from django.db import models
from django.db.models import (CharField, BooleanField, DateTimeField,
                              TextField, URLField, UUIDField)

from utility import get_random_string_for_url


# Create your models here.
class OtherField(models.Model):
    status = BooleanField(default=True, null=True)
    deleted = BooleanField(default=False, null=True)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Url(OtherField):
    original_url = URLField(unique=True)
    short_url = CharField(max_length=32, default=get_random_string_for_url, editable=False, unique=True)

    def to_dict(self):
        return {
            "original_url": self.original_url,
            "short_url": self.short_url
        }
