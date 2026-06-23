
from rest_framework import serializers

from chats.models import Message

class MessageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = "__all__"


class MessageRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = "__all__"


class MessageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = "__all__"

    
class MessageUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = "__all__"