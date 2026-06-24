from django.db import transaction
from rest_framework.exceptions import ValidationError

from modules.chats.models import Conversation, User, Participants
from modules.chats.common.enums import ConversationEnums, RoleEnums

class ConversationService:

    @staticmethod
    @transaction.atomic
    def direct_create(*, request, serializer, data):
        serializer = serializer(
            data=data
        )

        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        user1, user2 = sorted(data.get("users"))

        direct_key = f"{user1}:{user2}"
        
        conversation, created = Conversation.objects.get_or_create(
            direct_key=direct_key,
            defaults={
                "type": ConversationEnums.DIRECT
            }
        )

        if created:
            users = User.objects.filter(
                id__in=data.get("users")
            )

            # if User.objects.filter(
            #     id__in=data.get("users")
            # ).count()<2:
            #     raise ValidationError({
            #         "detail": "User does not exist."
            #     })

            participants = []

            for user in users:
                participants.append(
                    Participants(
                        conversation=conversation,
                        user=user,
                        role=RoleEnums.OWNER
                    )
                )

            if participants:
                Participants.objects.bulk_create(participants)
        
        return conversation


    @staticmethod
    def update(*, request, serializer, data, id):
        ...

