from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import BankSerializer, AccountSerializer
from .models import Bank

# Create your views here.

class BankView(viewsets.ModelViewSet):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()

class AccountView(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = AccountSerializer

    def get_queryset(self):
        return self.request.user.holders.all()

    def perform_create(self, serializer):
        serializer.save(holder=self.request.user)