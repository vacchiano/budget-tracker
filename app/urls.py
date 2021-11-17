from django.urls import path
from .views import dashboard, transactions, TransactionCreateView, TransactionDeleteView, TransactionUpdateView, TransactionDetailView

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('transactions/', transactions, name='transactions'),
    path('transaction/<int:pk>/detail/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('transaction/create/', TransactionCreateView.as_view(), name='transaction-create'),
    path('transaction/<int:pk>/update/', TransactionUpdateView.as_view(), name='transaction-update'),
    path('transaction/<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction-delete'),
]