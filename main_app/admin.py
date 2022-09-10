from django.contrib import admin
from .models import userProfile, balanceRecord, transaction

admin.site.register(userProfile)
admin.site.register(balanceRecord)
admin.site.register(transaction)
