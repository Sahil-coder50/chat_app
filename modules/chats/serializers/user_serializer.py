from rest_framework import serializers
from modules.chats.models import User

class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

class UserRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class UserSerializer(serializers.Serializer):
    users = serializers.ListField()

    def validate_users(self, attr):
        if len(attr)<2:
            raise serializers.ValidationError(
                "Need two users minimum for DIRECT conversation"
            )
        elif len(attr)>2:
            raise serializers.ValidationError(
                "Maximum two users are allowed for DIRECT conversation"
            )
        
        if User.objects.filter(id__in = attr).count()<2:
            raise serializers.ValidationError(
                "User Id not Valid - No user exist with this Id."
            )
        
        return attr
