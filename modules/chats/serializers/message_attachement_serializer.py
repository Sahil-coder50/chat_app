from rest_framework import serializers
from modules.chats.models import MessageAttachement

class MessageAttachementCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageAttachement
        fields = "__all__"

class MessageAttachementUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageAttachement
        fields = "__all__"

class MessageAttachementListSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageAttachement
        fields = "__all__"

class MessageAttachementRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageAttachement
        fields = "__all__"
