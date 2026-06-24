
from rest_framework.decorators import action
from rest_framework import status

from modules.chats.common.base.view import BaseAPIView
from modules.chats.models import User, Conversation, Participants
from modules.chats.common.enums import ConversationEnums, RoleEnums

from modules.chats.services import ConversationService
from modules.chats.selectors import ConversationSelector
from modules.chats.serializers import UserSerializer, ConversationCreateSerializer, ConversationListSerializer, ConversationUpdateSerializer, ConversationRetrieveSerializer


class ConversationViewSet(BaseAPIView):

    @action(detail=False, methods=["POST"])
    def direct(self, request):
        conversation = ConversationService.direct_create(request=request, serializer=UserSerializer, data=request.data)

        return self.success_response(
            data=conversation.id,
            status=status.HTTP_201_CREATED
        )


    @action(detail=False, methods=["POST"])
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



