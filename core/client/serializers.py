from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        read_only_fields = ('created_by', 'created_at',)
        fields = (
            'id',
            'name',
            'email',
            'CIN',
            'address1',
            'address2',
            'pincode',
            'place',
            'country',
            'country_person',
            'country_reference',
        )
