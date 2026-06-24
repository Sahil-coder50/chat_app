from django.db import models
from modules.chats.common.enums import RoleEnums

class Participants(models.Model):
    conversation = models.ForeignKey(
        "Conversation",
        on_delete=models.CASCADE,
        related_name="members"
    )

    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="conversation_members",
    )

    role = models.CharField(
        max_length=10,
        choices=RoleEnums,
        default=RoleEnums.MEMBER,
    )

    last_read_message = models.ForeignKey(
        "Message",
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )

    joined_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    muted_until = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("conversation", "user")
