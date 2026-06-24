from modules.chats.models import Conversation

class ConversationSelector:

    @staticmethod
    def list(*, request, serializer):
        ...

    @staticmethod
    def retrieve(*, request, serializer, id):
        ...