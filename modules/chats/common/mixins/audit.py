from chats.models import User
from django.db import models

class AuditMixin:
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True, blank=True
    )