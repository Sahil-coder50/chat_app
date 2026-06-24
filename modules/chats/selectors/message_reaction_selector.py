from modules.chats.models import MessageReaction

class MessageReactionSelector:

    @staticmethod
    def list(*, request, serializer):
        ...

    @staticmethod
    def retrieve(*, request, serialzier, id):
        ...
