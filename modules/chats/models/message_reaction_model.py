from django.db import models

class MessageReaction(models.Model):
    message = models.ForeignKey(
        "Message",
        on_delete=models.CASCADE,
        related_name="reactions",
    )

    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="message_reactions",
    )

    emoji = models.CharField(max_length=20)

    class Meta:
        unique_together = (
            "message",
            "user",
            "emoji",
        )