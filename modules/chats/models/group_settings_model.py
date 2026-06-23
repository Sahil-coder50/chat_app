from django.db import models

class GroupSettings(models.Model):
    conversation = models.OneToOneField(
        "Conversation",
        on_delete=models.CASCADE,
        related_name="settings",
    )

    description = models.TextField(blank=True, null=True)

    avatar = models.ImageField(
        upload_to="group_avatars/",
        null=True, blank=True,
    )

    invite_link = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    