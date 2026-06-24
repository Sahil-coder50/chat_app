from modules.chats.models import MessageRead

class MessageReadSelector:

    @staticmethod
    def list(*, request, serializer):
        ...

    @staticmethod
    def retrieve(*, request, serializer, id):
        ...