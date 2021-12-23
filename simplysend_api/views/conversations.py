from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from ..serializers.conversation import ConversationSerializer
from ..models.conversation import Conversation

class ListConversations(generics.ListAPIView):
    def get(self, request):
        conversations = Conversation.objects.filter(participants__id=request.user.id)
        data = ConversationSerializer(conversations, many=True).data
        return Response(data)

class CreateConversation(APIView):
    def post(self, request):
        request.data['participants'] = [*request.data['participants'], request.user]
        conversation = ConversationSerializer(data=request.data)
        if conversation.is_valid():
            conversation.save()
            return Response(conversation.data, status=status.HTTP_201_CREATED)
        else:
            return Response(conversation.errors, status=status.HTTP_400_BAD_REQUEST)

class OneConversation(APIView):
    def get(self, request, id):
        conversation = get_object_or_404(Conversation, pk=id)
        data = ConversationSerializer(conversation).data
        return Response(data)

class DeleteConversation(APIView):
    def delete(self, request, id):
        conversation = get_object_or_404(Conversation, pk=id)
        conversation.delete()
        # check = True
        # for participant in conversation['participants']:
        #     if participant != request.user.email:
        #         check = False
        # if not check:
        #     raise PermissionDenied('Unauthorized, you are not apart of this conversation')
        # else:
        #     conversation.delete()
        #     return Response('Conversation Deleted', status=status.HTTP_204_NO_CONTENT)
        return Response('Conversation deleted', status=status.HTTP_204_NO_CONTENT)