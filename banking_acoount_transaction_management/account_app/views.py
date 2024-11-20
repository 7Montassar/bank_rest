from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Client, Account, Bank, Transaction
from .serializers import ClientSerializer, AccountSerializer, BankSerializer, TransactionSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'cin'  


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'rib'  # Allow querying by RIB

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
