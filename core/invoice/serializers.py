from rest_framework import serializers
from .models import Invoice, Item


class InvoiceSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()

    class Meta:
        model = Invoice
        read_only_fields = (
            "teams", "created_at", "created_by", "modified_at", "modified_by",
        )

        fields = (
            "invoice_number",
            "client_CIN",
            "client_address1",
            "client_address2",
            "client_pincode",
            "client_place",
            "client_country",
            "client_country_person",
            "client_country_reference",
            "invoice_type",
            "due_days",
            "is_credit_for",
            "is_send",
            "is_paid",
            "gross_amount",
            "tax_amount",
            "net_amount",
            "discount_amount",
            "team",
            "client",
        )


class ItemSerializer(serializers.ModelField):
    class Meta:
        model = Item
        read_only_fields = (
            "invoices",
        )

        fields = (
            "id",
            "invoice",
            "title",
            "quantity",
            "unit_price",
            "tax_rate",
            "discount",
        )
