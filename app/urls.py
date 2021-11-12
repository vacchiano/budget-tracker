from django.urls import path
from .views import dashboard, transactions, TransactionCreateView

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('transactions/', transactions, name='transactions'),
    path('transaction/create', TransactionCreateView.as_view(), name='transaction-create'),
]