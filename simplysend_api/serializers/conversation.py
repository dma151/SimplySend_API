from rest_framework import serializers
from ..models.conversation import Conversation
from ..serializers.message import MessageSerializer

class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = Conversation
        fields = ('id', 'participants', 'messages')