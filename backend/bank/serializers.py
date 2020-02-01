from rest_framework import serializers
from .models import Bank, Account

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('id', 'title', 'description', 'completed')

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        # fields = ['id', 'name', 'balance']
        fields = '__all__'
