# Generated by Django 3.2.8 on 2021-10-28 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('Housing', 'Housing'), ('Transportation', 'Transportation'), ('Food', 'Food'), ('Utilities', 'Utilities'), ('Insurance', 'Insurance'), ('Medical', 'Medical'), ('Savings', 'Savings'), ('Personal', 'Personal'), ('Entertainment', 'Entertainment'), ('Misc', 'Misc'), ('Income', 'Income')], max_length=100),
        ),
    ]
