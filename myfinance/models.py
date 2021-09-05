from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import HStoreField
from datetime import datetime

class PlaidItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE, default=None)
    access_token = models.CharField(max_length=200, unique=True)
    item_id = models.CharField(max_length=200, unique=True)

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    plaid_account_id = models.CharField(max_length=200, null=True, unique=True)
    balances = models.JSONField(null=True)
    mask = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    official_name = models.CharField(max_length=200, null=True)
    subtype = models.CharField(max_length=200, null=True)
    account_type = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE, default=None)
    item = models.ForeignKey(PlaidItem, on_delete=models.CASCADE, default=None, null=True, blank=True)

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    account_owner = models.CharField(max_length=200, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    authorized_date = models.CharField(max_length=200, null=True)
    category = ArrayField(models.CharField(max_length=200), null=True)
    category_id = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(null=False, default=datetime.now())
    iso_currency_code = models.CharField(max_length=200, null=True)
    location = models.JSONField(null=True)
    merchant_name = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    payment_meta = models.JSONField(null=True)
    payment_channel = models.CharField(max_length=200, null=True)
    pending = models.BooleanField(null=True)
    pending_transaction_id = models.CharField(max_length=200, null=True)
    transaction_code = models.CharField(max_length=200, null=True)
    transaction_id = models.CharField(max_length=200, unique=True, null=True, blank=False)
    transaction_type = models.CharField(max_length=200, null=True)
    unofficial_currency_code = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.transaction_text
