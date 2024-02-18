from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from api.exceptions import BadRequestException
from .models import Message, Category
from .serializers.serializers import CategorySerializer, MessageDetailSerializer, MessageSerializer
from .serializers.user_serializer import UserSerializer


class MessageView(APIView):

    # def get(self, request):
    #     print(request.COOKIES)
    #     test1 = request.COOKIES.get("test")
    #     test2 = request.COOKIES.get("test2")
    #     print(test1, test2)
    #     test = {"name": "Siron Shakya", "address": "Jawalakhel"}
    #     list_example = ['hello', '2']
    #     response = Response(list_example, 200)
    #     response.set_cookie("token", "randomtest2",
    #                         max_age=3600, secure=True, httponly=False)
    #     return response

    def get(self, request, pk=None):
        if pk is None:
            message = Message.objects.all()
            serializer = MessageSerializer(message, many=True)
        else:
            message = Message.objects.get(message_id=pk)
            serializer = MessageSerializer(message)
        return Response(serializer.data, 200)

    def post(self, request):
        message = MessageSerializer(data=request.data)
        message_detail = MessageDetailSerializer(
            data=request.data.get("message_detail"))

        try:
            user = User.objects.get(id=request.data.get("user_id"))
        except ObjectDoesNotExist as e:
            raise ObjectDoesNotExist("User Not Found")

        if message_detail.is_valid():
            saved_message_detail = message_detail.save()
            if message.is_valid():
                message.save(user=user, message_detail=saved_message_detail)
                return Response("Message saved", 201)

        raise BadRequestException()


class UserView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            user = User.objects.get(id=pk)
            user_serializer = UserSerializer(user)

            return Response(user_serializer.data, 200)
        raise BadRequestException()


class CategoryView(APIView):

    def get(self, request):
        category = Category.objects.all()
        return Response(CategorySerializer(category, many=True).data, 200)

    def post(self, request):
        category = CategorySerializer(data=request.data)
        if category.is_valid():
            category.save()
            return Response("Category saved", 201)

        raise BadRequestException()


@api_view(['GET'])
def add_category(request, message_id, category_id):
    try:
        category = Category.objects.get(category_id=category_id)
    except ObjectDoesNotExist as e:
        raise ObjectDoesNotExist("Category not found")

    try:
        message = Message.objects.get(message_id=message_id)
    except ObjectDoesNotExist as e:
        raise ObjectDoesNotExist("Message not found")

    message.category.add(category)

    return Response("Category addded to message")
