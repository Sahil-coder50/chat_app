
from rest_framework import serializers

from chats.models import Conversation
from chats.serializers import MessageSerializer

class ConversationRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conversation
        fields = "__all__"
