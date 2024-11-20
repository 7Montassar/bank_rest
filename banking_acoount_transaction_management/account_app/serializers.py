from rest_framework import serializers
from .models import Client, Account, Bank, Transaction, AccountType, TransactionType

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['cin', 'name', 'familyName', 'email']


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['id', 'name', 'address', 'creationDate']


class AccountSerializer(serializers.ModelSerializer):
    client = ClientSerializer()  

    class Meta:
        model = Account
        fields = ['rib', 'balance', 'client', 'creation_date', 'accountType']

    def create(self, validated_data):
        client_data = validated_data.pop('client')
        client, _ = Client.objects.get_or_create(cin=client_data['cin'], defaults=client_data)
        validated_data['client'] = client
        return Account.objects.create(**validated_data)


class TransactionSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'date', 'transactionType', 'account', 'transfer_to_account']

    def validate(self, data):
        account = data['account']
        if data['transactionType'] == TransactionType.WITHDRAW and data['amount'] > account.balance:
            raise serializers.ValidationError(f"You can't withdraw more than {account.balance}.")
        if data['transactionType'] == TransactionType.TRANSFER and not data.get('transfer_to_account'):
            raise serializers.ValidationError("You must specify the RIB to transfer to.")
        return data
