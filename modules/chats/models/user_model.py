from django.db import models
from chats.common.mixins import SoftDeleteMixin, TimestampMixin

class User(models.Model, SoftDeleteMixin, TimestampMixin):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    status = models.BooleanField(default=True)

    last_seen_at = models.DateTimeField(null=True, blank=True)
