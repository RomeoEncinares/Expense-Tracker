from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class userProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    currentBalance = models.FloatField(default=0)

    def addTransaction(self, type, cost):
        if type == "Income":
            self.currentBalance += cost
        else:
            self.currentBalance -= cost

    def __str__(self):
        return str(self.username)

class balanceRecord(models.Model):
    username = models.ForeignKey(userProfile, on_delete=models.CASCADE)
    balance  = models.FloatField(default=0)
    date = models.DateField(default=now)

    def _str__(self):
        return "{} {:.2f} {}".format(self.username, self.balance, self.date)

class transaction(models.Model):
    username = models.ForeignKey(userProfile, on_delete=models.CASCADE)
    TRANSACTION_CHOICES = (('Income', 'Income'), ('Expense', 'Expense'))
    transactionType = models.CharField(max_length=10, choices=TRANSACTION_CHOICES)
    CATEGORY_CHOICES = (
        ('Food & Drinks', 'Food & Drinks'),
        ('Shopping', 'Shopping'),
        ('Housing', 'Housing'),
        ('Transportation', 'Transportation'),
        ('Vehicle', 'Vehicle'),
        ('Life & Entertainment', 'Life & Entertainment'),
        ('PC, Communication', 'PC, Communication'),
        ('Financial Investment', 'Financial Investment'),
        ('Investment', 'Investment'),
        ('Income', 'Income'),
        ('Others', 'Others'),
    )
    transactionCategory = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField(default=now)
    amount = models.FloatField()

    def __str__(self):
        return "{} {} {} {:.2f}".format(self.username, self.transactionType, self.transactionCategory, self.amount)