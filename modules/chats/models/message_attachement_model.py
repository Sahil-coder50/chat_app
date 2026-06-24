from django.db import models
from modules.chats.common.enums import MessageTypeEnums

class MessageAttachement(models.Model):
    message = models.ForeignKey(
        "Message",
        on_delete=models.CASCADE,
        related_name="attachements"
    )

    file = models.FileField(upload_to="chat/")

    type = models.CharField(
        max_length=10,
        choices=MessageTypeEnums,
    )

    size = models.BigIntegerField()
    