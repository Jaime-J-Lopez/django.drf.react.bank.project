from rest_framework import serializers
from .models import Bank, Account

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('id', 'title', 'description', 'completed')

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['id', 'name']
        model = Account