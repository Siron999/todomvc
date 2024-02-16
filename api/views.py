from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer


class MessageView(APIView):

    # def get(self, request):
    #     print(request.COOKIES)
    #     test1 = request.COOKIES.get("test")
    #     test2 = request.COOKIES.get("test2")
    #     print(test1, test2)
    #     test = {"name": "Siron Shakya", "address": "Jawalakhel"}
    #     list_example = ['hello', '2']
    #     response = Response(list_example, 200)
    #     response.set_cookie("token", "randomtest",
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
        if message.is_valid():
            message.save()
        return Response("Message saved")
