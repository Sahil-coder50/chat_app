
from rest_framework.decorators import action
from rest_framework import status

from chats.common.base.view import BaseAPIView
from chats.models import User, Conversation, Participants
from chats.common.enums import ConversationEnums, RoleEnums


class ConversationViewSet(BaseAPIView):
    
    def create(self, request):
        ...

    @action(details=False, methods=["POST"])
    def direct(self, request):
        conversation = Conversation.objects.create(
            type=ConversationEnums.DIRECT,
        )

        Participants.objects.create(
            conversation=conversation,
            user=request.user,
            role=RoleEnums.OWNER
        )

        user = User.objects.filter(
            id=request.data.user_id
        )

        Participants.objects.create(
            conversation=conversation,
            user=user,
            role=RoleEnums.OWNER
        )

        return self.success_response(
            data=conversation.id,
            status=status.HTTP_200_OK
        )


    @action(details=False, methods=["POST"])
    def group(self, request):
        ...

    def update(self, request, id):
        ...

    def retrieve(self, request, id):
        conversation = Conversation.objects.filter(
            id=id
        )
    
    def list(self, request):
        conversations = Conversation.objects.filter(
            members_user=request.user,
        ).distinct()



