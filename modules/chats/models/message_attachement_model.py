from django.db import models
from chats.common.enums import MessageTypeEnums

class MessageAttachement(models.Model):
    message = models.ForeignKey(
        "Message",
        on_delete=models.CASCADE,
        related_name="attachements"
    )

    file = models.ForeignKey(upload_to="chat/")

    type = models.CharField(
        max_length=10,
        choices=MessageTypeEnums,
    )

    size = models.BigIntegerField()
    