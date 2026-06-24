from modules.chats.models import Message

class MessageSelector:

    @staticmethod
    def list(*, request, serializer):
        ...

    @staticmethod
    def retrieve(*, request, serializer, id):
        ...
