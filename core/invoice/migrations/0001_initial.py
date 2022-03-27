# Generated by Django 4.0.2 on 2022-02-27 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.IntegerField(default=1000)),
                ('client_name', models.CharField(max_length=255)),
                ('client_email', models.EmailField(max_length=254)),
                ('client_CIN', models.CharField(blank=True, max_length=255, null=True)),
                ('client_address1', models.TextField(blank=True, null=True)),
                ('client_address2', models.TextField(blank=True, null=True)),
                ('client_pincode', models.IntegerField(blank=True, null=True)),
                ('client_place', models.CharField(blank=True, max_length=255, null=True)),
                ('client_country', models.CharField(blank=True, max_length=255, null=True)),
                ('client_country_person', models.CharField(blank=True, max_length=255, null=True)),
                ('client_country_reference', models.CharField(blank=True, max_length=255, null=True)),
                ('invoice_type', models.CharField(choices=[('Invoice', 'Invoice'), ('Credit note', 'Credit note')], default='Invoice', max_length=20)),
                ('due_days', models.IntegerField(default=14)),
                ('is_send', models.BooleanField(default=False)),
                ('is_paid', models.BooleanField(default=False)),
                ('gross_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tax_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('net_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('discount_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='client.client')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_invoices', to=settings.AUTH_USER_MODEL)),
                ('is_credit_for', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoice.invoice')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_invoices', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='team.team')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(default=1)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('net_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tax_rate', models.IntegerField(default=0)),
                ('discount', models.IntegerField(default=0)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='invoice.invoice')),
            ],
        ),
    ]
