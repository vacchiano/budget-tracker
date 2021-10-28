from django.contrib.auth import get_user_model
from django.shortcuts import render
from .models import Transaction
from datetime import datetime


User = get_user_model()

def dashboard(request):
    current_month = datetime.now().month
    # transactions = Transaction.objects.filter(owner=request.user, date__month=current_month).order_by('-date')
    transactions = Transaction.objects.filter(owner=request.user).order_by('-date')[:10]
    context = {
        'transactions': transactions
    }
    return render(request, 'app/index.html', context)