
from rest_framework import serializers

from chats.models import Conversation

class ConversationListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conversation
        fields = "__all__"


class ConversationRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conversation
        fields = "__all__"


class ConversationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conversation
        fields = "__all__"


class ConversationUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conversation
        fields = "__all__"
