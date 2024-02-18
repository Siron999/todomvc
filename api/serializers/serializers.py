from rest_framework import serializers


from ..models import Message, MessageDetail, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['category_id', 'name']


class MessageDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageDetail
        fields = ['detail']


class MessageSerializer(serializers.ModelSerializer):
    message_detail = MessageDetailSerializer(
        many=False, required=False)

    class Meta:
        model = Message
        fields = ['message_id', 'title', 'body', 'created_at',
                  'updated_at', 'message_detail', 'category']
