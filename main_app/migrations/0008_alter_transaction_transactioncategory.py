# Generated by Django 3.2.4 on 2022-09-08 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_transaction_transactiontype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transactionCategory',
            field=models.CharField(choices=[('Food & Drinks', 'Food & Drinks'), ('Shopping', 'Shopping'), ('Housing', 'Housing'), ('Transportation', 'Transportation'), ('Vehicle', 'Vehicle'), ('Life & Entertainment', 'Life & Entertainment'), ('PC, Communication', 'PC, Communication'), ('Financial Investment', 'Financial Investment'), ('Investment', 'Investment'), ('Income', 'Income'), ('Others', 'Others')], max_length=20),
        ),
    ]
