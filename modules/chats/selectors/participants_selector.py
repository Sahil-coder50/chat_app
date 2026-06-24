from modules.chats.models import Participants

class ParticipantsSelector:

    @staticmethod
    def list(*, request, serializer):
        ...

    @staticmethod
    def retrieve(*, request, serializer, id):
        ...