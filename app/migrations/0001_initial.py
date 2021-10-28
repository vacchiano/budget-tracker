# Generated by Django 3.2.8 on 2021-10-28 04:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('Expense', 'Expense'), ('Income', 'Income')], max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('category', models.CharField(choices=[('Housing', 'Housing'), ('Transportation', 'Transportation'), ('Food', 'Food'), ('Utilities', 'Utilities'), ('Insurance', 'Insurance'), ('Medical', 'Medical'), ('Savings', 'Savings'), ('Personal', 'Personal'), ('Entertainment', 'Entertainment'), ('Misc', 'Misc')], max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
