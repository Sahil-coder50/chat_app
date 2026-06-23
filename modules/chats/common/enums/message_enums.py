from django.db import models

class MessageTypeEnums(models.TextChoices):
    TEXT = ("text", "Text")
    IMAGE = ("image", "Image")
    VIDEO = ("video", "Video")
    FILE = ("file", "File")
    SYSTEM = ("system", "System")
