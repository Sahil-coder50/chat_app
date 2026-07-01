from django.db import models
from modules.chats.common.mixins import SoftDeleteMixin, TimestampMixin
from auth_drf.models.user_model import BaseUser

class User(BaseUser, SoftDeleteMixin, TimestampMixin):
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    status = models.BooleanField(default=True)

    last_seen_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = False
