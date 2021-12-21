from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from django.core.exceptions import AppRegistryNotReady, PermissionDenied
from ..serializers.message import MessageSerializer
from ..models.message import Message

class NewMessage(APIView):
    def post(self, request):
        request.data['author'] = request.user.id
        message = MessageSerializer(data=request.data)
        if message.is_valid():
            message.save()
            return Response(message.data, status=status.HTTP_201_CREATED)
        else:
            return Response(message.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteMessage(APIView):
    def delete(self, request, id):
        message = get_object_or_404(Message, pk=id)
        if request.user != message.author:
            raise PermissionDenied('Unauthorized, you did not write this message')
        message.delete()
        return Response('Message deleted', status=status.HTTP_204_NO_CONTENT)

class EditMessage(APIView):
    def patch(self, request, id):
        message = get_object_or_404(Message, pk=id)
        if request.user != message.author:
            raise PermissionDenied('Unauthorized, you did not write this message')
        update_message = MessageSerializer(message, data=request.data, partial=True)
        if update_message.is_valid():
            update_message.save()
            return Response(update_message.data)
        else:
            return Response(update_message.errors, status=status.HTTP_400_BAD_REQUEST)
