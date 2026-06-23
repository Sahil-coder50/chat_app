from django.db import models

class MessageRead(models.Model):
    message = models.ForeignKey(
        "Message",
        on_delete=models.CASCADE,
        related_name="reads",
    )

    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="read_messages",
    )

    read_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together= ("message", "user") 