from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils import timezone

from .models import Transaction
from .forms import TransactionForm
from config.settings import MONTHS

User = get_user_model() #gets user model imported

@login_required
def dashboard(request):
    current_month = timezone.now().month
    current_year = timezone.now().year
    # transactions = Transaction.objects.filter(owner=request.user, date__month=current_month).order_by('-date')
    transactions = Transaction.objects.filter(owner=request.user).order_by('-date')

    monthly_income = Transaction.objects.filter(owner=request.user, type="Income", date__month=current_month, date__year=current_year)
    monthly_income = monthly_income.aggregate(Sum('amount'))['amount__sum']

    monthly_expenses = Transaction.objects.filter(owner=request.user, type="Expense", date__month=current_month, date__year=current_year)
    monthly_expenses = monthly_expenses.aggregate(Sum('amount'))['amount__sum']


    categories = []
    for category in Transaction.CATEGORY_CHOICES:
        category_sum_amount = Transaction.objects.filter(owner=request.user, type='Expense', date__month=current_month, date__year=current_year, category=category[0])
        category_sum_amount = category_sum_amount.aggregate(Sum('amount'))['amount__sum']
        categories.append({
            'category': category[0],
            'amount': category_sum_amount
            })

    context = {
        'transactions': transactions[:10],
        'current_month': timezone.now(),
        'categories_data': categories,
        'monthly_data': [{
            "monthly_income": monthly_income,
            "monthly_expenses": monthly_expenses
            }]
    }
    return render(request, 'app/index.html', context)

@login_required
def transactions(request):
    transactions = Transaction.objects.filter(owner=request.user).order_by('-date')
    context = {
        'transactions': transactions
    }
    return render(request, 'app/transactions.html', context)

class TransactionDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Transaction

    # checks whether the logged in user is the owner of the transaction
    def test_func(self):
        transaction = self.get_object()
        if self.request.user == transaction.owner:
            return True
        return False

class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    #fields = ['date', 'type', 'amount', 'description', 'category']
    form_class = TransactionForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form) #running form valid method from parent class

    def get_success_url(self):
        return reverse('transactions')

class TransactionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name_suffix = '_update'

    # checks whether the logged in user is the owner of the transaction
    def test_func(self):
        transaction = self.get_object()
        if self.request.user == transaction.owner:
            return True
        return False

class TransactionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Transaction
    context_object_name = 'transaction'
    success_url = reverse_lazy('transactions')

    # checks whether the logged in user is the owner of the transaction
    def test_func(self):
        transaction = self.get_object()
        if self.request.user == transaction.owner:
            return True
        return False
