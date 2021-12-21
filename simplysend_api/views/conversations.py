from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from ..serializers.conversation import ConversationSerializer
from ..models.conversation import Conversation

class ListConversations(generics.ListAPIView):
    def get(self, request):
        conversations = Conversation.objects.filter(participants__id=request.user.id)
        data = ConversationSerializer(conversations, many=True).data
        return Response(data)

class CreateConversation(APIView):
    def post(self, request):
        users = [request.user.id, *request.data['participants']]
        conversation = ConversationSerializer(data=request.data)
        if conversation.is_valid():
            conversation.save()
            return Response(conversation.data, status=status.HTTP_201_CREATED)
        else:
            return Response(conversation.errors, status=status.HTTP_400_BAD_REQUEST)