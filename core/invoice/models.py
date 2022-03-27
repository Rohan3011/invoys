from django.db import models
from accounts.models import UserAccount as User

from client.models import Client
from team.models import Team


class Invoice(models.Model):
    INVOICE = 'Invoice'
    CREDIT_NOTE = 'Credit note'

    CHOICES_TYPE = (
        (INVOICE, 'Invoice'),
        (CREDIT_NOTE, 'Credit note')
    )

    invoice_number = models.IntegerField(default=1000)
    client_name = models.CharField(max_length=255)
    client_email = models.EmailField()
    # Corporate Identification Number
    client_CIN = models.CharField(max_length=255, blank=True, null=True)
    client_address1 = models.TextField(blank=True, null=True)
    client_address2 = models.TextField(blank=True, null=True)
    client_pincode = models.IntegerField(blank=True, null=True)
    client_place = models.CharField(max_length=255, blank=True, null=True)
    client_country = models.CharField(max_length=255, blank=True, null=True)
    client_country_person = models.CharField(
        max_length=255, blank=True, null=True)
    client_country_reference = models.CharField(
        max_length=255, blank=True, null=True)
    invoice_type = models.CharField(
        max_length=20, choices=CHOICES_TYPE, default=INVOICE)
    due_days = models.IntegerField(default=14)
    is_credit_for = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True)
    is_send = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    gross_amount = models.DecimalField(max_digits=6, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=6, decimal_places=2)
    net_amount = models.DecimalField(max_digits=6, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=6, decimal_places=2)
    team = models.ForeignKey(
        Team, related_name="invoices", on_delete=models.CASCADE)
    client = models.ForeignKey(
        Client, related_name="invoices", on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, related_name="created_invoices", on_delete=models.CASCADE)
    modified_by = models.ForeignKey(
        User, related_name="modified_invoices", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Item(models.Model):
    invoice = models.ForeignKey(
        Invoice, related_name="items", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    net_amount = models.DecimalField(max_digits=6, decimal_places=2)
    tax_rate = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
