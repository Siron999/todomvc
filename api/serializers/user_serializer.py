from rest_framework.fields import empty
from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import Message

from api.serializers.serializers import MessageSerializer


class UserSerializer(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ['password']

    def get_messages(self, obj):
        message = obj.message_set.all()
        serializer = MessageSerializer(message, many=True)
        return serializer.data
