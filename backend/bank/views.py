from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BankSerializer
from .models import Bank
# Create your views here.

class BankView(viewsets.ModelViewSet):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()