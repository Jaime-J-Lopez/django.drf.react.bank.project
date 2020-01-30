from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, PasswordSerializer, GroupSerializer
from bank.models import Account
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.generics import
from bank.serializers import AccountSerializer
# Create your views here.

class AccountView(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    # serializer_class = AccountSerializer
    #
    # def get_queryset(self):
    #     return self.request.user.holders.all()
    #
    # def perform_create(self, serializer):
    #     serializer.save(holder=self.request.user)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

class PasswordAPIView(APIView):
    def get_object(self, username):
        user = get_object_or_404(User, username=username)
        return user
    def put(self, request):
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            user = self.get_object(username)
            new_password = serializer.data['password']
            is_same_as_old = user.check_password(new_password)
            if is_same_as_old:
                """
                old password and new passwords should not be the same
                """
                return Response({"password": ["It should be different from your last password."]},
                                status=status.HTTP_400_BAD_REQUEST)
            user.set_password(new_password)
            user.save()
            return Response({'success':True})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)