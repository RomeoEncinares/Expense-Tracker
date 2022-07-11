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
