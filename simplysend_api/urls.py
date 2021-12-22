from django.urls import path
from .views.users import SignUp, SignIn, SignOut, ChangePassword, Friends, GetUser
from .views.friend_requests import MakeFriendRequest, FriendRequests, AcceptFriendRequest, DeleteFriendRequest, PendingFriendRequests
from .views.conversations import ListConversations, CreateConversation, OneConversation, DeleteConversation
from .views.messages import NewMessage, DeleteMessage, EditMessage

urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),
    path('get-user/<int:id>/', GetUser.as_view(), name='get-user-by-id'),
    path('make-friend-request/<str:email>/', MakeFriendRequest.as_view(), name='make-friend-request'),
    path('accept-friend-request/<int:id>/', AcceptFriendRequest.as_view(), name='accept-friend-request'),
    path('delete-friend-request/<int:id>/', DeleteFriendRequest.as_view(), name='delete-friend-request'),
    path('friend-requests/', FriendRequests.as_view(), name='friend-requests'),
    path('pending-friend-requests/', PendingFriendRequests.as_view(), name='pending-friend-requests'),
    path('friends/', Friends.as_view(), name='friends'),
    path('conversations/', ListConversations.as_view(), name='conversations index'),
    path('conversations/create/', CreateConversation.as_view(), name='create-conversation'),
    path('conversations/<int:id>/', OneConversation.as_view(), name='conversation by id'),
    path('conversations/delete/<int:id>/', DeleteConversation.as_view(), name='delete-conversation'),
    path('messages/', NewMessage.as_view(), name='new-message'),
    path('messages/delete/<int:id>/', DeleteMessage.as_view(), name='delete-message'),
    path('messages/<int:id>/', EditMessage.as_view(), name='edit-message')
]