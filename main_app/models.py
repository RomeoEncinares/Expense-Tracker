from django.db import models
from django.contrib.auth.models import User

class userProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username)
