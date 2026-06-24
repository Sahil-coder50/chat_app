from rest_framework import serializers
from modules.chats.models import MessageRead

class MessageReadCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageRead
        fields = "__all__"

class MessageReadUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageRead
        fields = "__all__"

class MessageReadListSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageRead
        fields = "__all__"

class MessageReadRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageRead
        fields = "__all__"
