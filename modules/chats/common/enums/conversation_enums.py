from django.db import models

class ConversationEnums(models.TextChoices):
    DIRECT = ("direct", "Direct")
    GROUP = ("group", "Group")
    CHANNEL = ("channel", "Channel")
