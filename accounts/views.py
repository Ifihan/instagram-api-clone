from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import AppUser
from accounts.serializers import LoginSerializer, RegistrationSerializer, AppUserSerializer


# Create your views here.
class RegisterView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class LoginView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def get_token(self, obj):
        user = AppUser.objects.filter(email=obj.get("email")).first()
        return user.token()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(self.get_token(serializer.data), status=status.HTTP_200_OK)


class AuthUserDataView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = AppUserSerializer(user)
        return Response(serializer.data)


# class MakeUserPrivateView(APIView):
#     permission_classes = (IsAuthenticated,)


# email authentication
# logout view
# password reset view
# follow/unfollow view
# profile
# make profile public or private
# make post
# should break this into auth and acccounts app
