from django.db import models
from django.conf import settings

class Transaction(models.Model):
    TYPE_CHOICES = [
        ('Expense', 'Expense'),
        ('Income', 'Income'),
    ]
    
    CATEGORY_CHOICES = [
        ('Housing', 'Housing'),
        ('Transportation', 'Transportation'),
        ('Food', 'Food'),
        ('Utilities', 'Utilities'),
        ('Insurance', 'Insurance'),
        ('Medical', 'Medical'),
        ('Savings', 'Savings'),
        ('Personal', 'Personal'),
        ('Entertainment', 'Entertainment'),
        ('Misc', 'Misc'),
        ('Income', 'Income'),
        ]

    date = models.DateField(auto_now=False, auto_now_add=False)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transactions')

    def __str__(self):
        if self.type == "Expense":
            return f'{self.description} | -${self.amount}'
        else:
            return f'{self.description} | ${self.amount}'
