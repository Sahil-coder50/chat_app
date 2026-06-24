from modules.chats.models import MessageAttachement

class MessageAttachementSelector:

    @staticmethod
    def list(*, request, serializer):
        ...

    @staticmethod
    def retrieve(*, request, serializer, id):
        ...
