from django.db import models
from chats.common.mixins import SoftDeleteMixin

class Message(models.Model, SoftDeleteMixin):
    conversation = models.ForeignKey(
        "Conversation",
        on_delete=models.CASCADE,
        related_name="messages",
    )
    sender_id = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="sent_messages",
    )

    content = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    is_edited = models.BooleanField(default=False)

    edited_at = models.DateTimeField(auto_now=True, null=True, blank=True)
