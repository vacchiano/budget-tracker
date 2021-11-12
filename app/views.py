from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView
from .models import Transaction
from datetime import datetime
from .forms import TransactionForm


User = get_user_model() #gets user model imported

def dashboard(request):
    current_month = datetime.now().month
    # transactions = Transaction.objects.filter(owner=request.user, date__month=current_month).order_by('-date')
    transactions = Transaction.objects.filter(owner=request.user).order_by('-date')[:10]
    context = {
        'transactions': transactions
    }
    return render(request, 'app/index.html', context)

def transactions(request):
    transactions = Transaction.objects.filter(owner=request.user).order_by('-date')
    context = {
        'transactions': transactions
    }
    return render(request, 'app/transactions.html', context)

class TransactionCreateView(CreateView):
    model = Transaction
    #fields = ['date', 'type', 'amount', 'description', 'category']
    form_class = TransactionForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form) #running form valid method on parent class

    def get_success_url(self):
        return reverse('transactions')
