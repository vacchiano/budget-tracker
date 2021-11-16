from django.urls import path
from .views import dashboard, transactions, TransactionCreateView, TransactionDeleteView

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('transactions/', transactions, name='transactions'),
    path('transaction/create', TransactionCreateView.as_view(), name='transaction-create'),
    path('transaction/<int:pk>/delete', TransactionDeleteView.as_view(), name='transaction-delete'),
]