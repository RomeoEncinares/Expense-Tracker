from django.db import models
from django.contrib.auth.models import User

class userProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)

    def addTransaction(self, type, cost):
        if type == "savings":
            self.balance += cost
        else:
            self.balance -= cost

    def __str__(self):
        return str(self.username)

class transaction(models.Model):
    username = models.ForeignKey(userProfile, on_delete=models.CASCADE)
    TRANSACTION_CHOICES = (('S', 'Savings'), ('E', 'Expenses'))
    transactionType = models.CharField(max_length=1, choices=TRANSACTION_CHOICES)
    CATEGORY_CHOICES = (
        ('FD', 'FOOD & DRINKS'),
        ('SH', 'SHOPPING'),
        ('HO', 'HOUSING'),
        ('TR', 'TRANSPORTATION'),
        ('VE', 'VEHICLE'),
        ('LE', 'LIFE & ENTERTAINMENT'),
        ('PC', 'PC, COMMUNICATION'),
        ('FE', 'FINANCIAL EXPENSES'),
        ('IV', 'INVESTMENT'),
        ('IC', 'INCOME'),
        ('OT', 'OTHERS'),
    )
    transactionCategory = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    amount = models.FloatField()

    def __str__(self):
        return "{} {} {} {:.2f}".format(self.username, self.transactionType, self.transactionCategory, self.amount)