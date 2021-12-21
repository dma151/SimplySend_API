from rest_framework import serializers
from django.shortcuts import get_object_or_404
from ..models.conversation import Conversation
from ..models.user import User
from .message import MessageSerializer
from .user import FriendSerializer

class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    participants = FriendSerializer(many=True)
    class Meta:
        model = Conversation
        fields = ('id', 'participants', 'messages')

    def create(self, validated_data):
        print(validated_data)
        participants = validated_data.pop('participants')
        conversation = Conversation()
        conversation.save()
        for email in participants:
            participant = get_object_or_404(User, email=email)
            conversation.participants.add(participant)
        conversation.save()
        return conversation