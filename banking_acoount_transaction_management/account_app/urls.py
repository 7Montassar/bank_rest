from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, AccountViewSet, BankViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'banks', BankViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),  
]
