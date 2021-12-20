from django.urls import path
from .views.users import SignUp, SignIn, SignOut, ChangePassword, MyFriends
from .views.friend_requests import MakeFriendRequest, MyFriendRequests, AcceptFriendRequest, DeleteFriendRequest, PendingFriendRequests

urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),
    path('make-friend-request/<str:email>/', MakeFriendRequest.as_view(), name='make-friend-request'),
    path('accept-friend-request/<int:id>/', AcceptFriendRequest.as_view(), name='accept-friend-request'),
    path('delete-friend-request/<int:id>/', DeleteFriendRequest.as_view(), name='delete-friend-request'),
    path('friend-requests/', MyFriendRequests.as_view(), name='friend-requests'),
    path('pending-friend-requests/', PendingFriendRequests.as_view(), name='pending-friend-requests'),
    path('my-friends/', MyFriends.as_view(), name='my-friends'),
]