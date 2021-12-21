from rest_framework.response import Response
from rest_framework import status, generics
from ..models.user import User
from ..models.friend_request import Friend_Request
from ..serializers.friend_request import Friend_RequestSerializer
from django.shortcuts import get_object_or_404

class MakeFriendRequest(generics.CreateAPIView):
    def post(self, request, email):
        from_user = request.user
        to_user = get_object_or_404(User, email=email)
        friend_request, created = Friend_Request.objects.get_or_create(from_user=from_user, to_user=to_user)
        if created:
            return Response('Friend request sent', status=status.HTTP_201_CREATED)
        else:
            return Response('Friend request was already sent', status=status.HTTP_400_BAD_REQUEST)

class AcceptFriendRequest(generics.CreateAPIView):
    def delete(self, request, id):
        friend_request = get_object_or_404(Friend_Request, pk=id)
        if friend_request.to_user == request.user:
            friend_request.to_user.friends.add(friend_request.from_user)
            friend_request.from_user.friends.add(friend_request.to_user)
            friend_request.delete()
            return Response('Friend Request accepted', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('Friend Request Not Accepted', status=status.HTTP_400_BAD_REQUEST)

class DeleteFriendRequest(generics.CreateAPIView):
    def delete(self, request, id):
        friend_request = get_object_or_404(Friend_Request, pk=id)
        if friend_request.to_user == request.user or friend_request.from_user == request.user:
            friend_request.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response('Unauthorized', status=status.HTTP_400_BAD_REQUEST)

class FriendRequests(generics.CreateAPIView):
    def get(self, request):
        friend_requests = Friend_Request.objects.filter(to_user = request.user)
        data = Friend_RequestSerializer(friend_requests, many=True).data
        return Response(data)

class PendingFriendRequests(generics.CreateAPIView):
    def get(self, request):
        friend_requests = Friend_Request.objects.filter(from_user = request.user)
        data = Friend_RequestSerializer(friend_requests, many=True).data
        return Response(data)