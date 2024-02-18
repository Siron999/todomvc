from rest_framework import serializers

# from api.serializers.user_serializer import UserSerializer
from ..models import Message


class MessageSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=False, required=False, allow_null=True)
    # details = MessageDetailSerializer(many=False, required=False)

    class Meta:
        model = Message
        fields = '__all__'
