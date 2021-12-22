from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from ..serializers.user import UserSerializer
from ..models.user import User
from ..models.friend_request import Friend_Request
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404

class SignUp(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

    def post(self, request):
        created_user = UserSerializer(data=request.data['user'])
        if created_user.is_valid():
            created_user.save()
            return Response({ 'user': created_user.data }, status=status.HTTP_201_CREATED)
        else:
            return Response(created_user.errors, status=status.HTTP_400_BAD_REQUEST)

class SignIn(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        data = request.data['user']
        user = authenticate(request, email=data['email'], password=data['password'])
        if user is not None:
            login(request, user)
            token = Token.objects.create(user=user)
            user.token = token.key
            user.save()
            return Response({
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'token': token.key
                }
            })
        else:
            return Response({'msg':'The username and/or password is incorrect.'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
class SignOut(generics.DestroyAPIView):
    def delete(self, request):
        user = request.user
        # Remove this token from the user
        Token.objects.filter(user=user).delete()
        user.token = None
        user.save()
        # Logout will remove all session data
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ChangePassword(generics.UpdateAPIView):
    def patch(self, request):
        user = request.user
        old_pw = request.data['passwords']['old']
        new_pw = request.data['passwords']['new']
        # This is included with the Django base user model
        # https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#django.contrib.auth.models.User.check_password
        if not user.check_password(old_pw):
            return Response({ 'msg': 'Wrong password' }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        # set_password will also hash the password
        # https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#django.contrib.auth.models.User.set_password
        user.set_password(new_pw)
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Friends(generics.CreateAPIView):
    def get(self, request):
        info = get_object_or_404(User, user=request.user)
        data = UserSerializer(info).data
        return Response(data)

class GetUser(generics.CreateAPIView):
    def get(self, request, id):
        info = get_object_or_404(User, pk=id)
        data = UserSerializer(info).data
        return Response(data)