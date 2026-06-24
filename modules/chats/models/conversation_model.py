from django.db import models
from modules.chats.common.enums import ConversationEnums
from modules.chats.common.mixins import SoftDeleteMixin, TimestampMixin, AuditMixin

class Conversation(models.Model, TimestampMixin, AuditMixin):
    type = models.CharField(
        max_length=10,
        choices=ConversationEnums,
        default=ConversationEnums.DIRECT,
    )
    title = models.CharField(
        max_length=255,
        blank=True, null=True,
    )

    direct_key = models.CharField(
        max_length=255,
        unique=True,
        null=True, blank=True,
    )
