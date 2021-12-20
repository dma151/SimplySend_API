from rest_framework import serializers
from ..models.friend_request import Friend_Request

class Friend_RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend_Request
        fields = '__all__'