from rest_framework import serializers

from .models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        read_only_fields = (
            'created_by',
        )
        fields = (
            'id', 'name', 'CIN', 'first_invoice_number',
        )
