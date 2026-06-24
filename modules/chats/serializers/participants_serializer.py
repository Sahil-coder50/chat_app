from rest_framework import serializers
from modules.chats.models import Participants

class ParticipantsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participants
        fields = "__all__"

class ParticipantsUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participants
        fields = "__all__"

class ParticipantsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participants
        fields = "__all__"

class ParticipantsRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participants
        fields = "__all__"
