from django.db import models

class RoleEnums(models.TextChoices):
    MEMBER = ("member", "Member")
    ADMIN = ("admin", "Admin")
    OWNER = ("owner", "Owner")
