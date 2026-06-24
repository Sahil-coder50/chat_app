from rest_framework import serializers
from modules.chats.models import MessageReaction

class MessageReactionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageReaction
        fields = "__all__"

class MessageReactionUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageReaction
        fields = "__all__"

class MessageReactionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageReaction
        fields = "__all__"

class MessageReactionRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageReaction
        fields = "__all__"
