from django.db import models
from accounts.models import UserAccount


class Team(models.Model):
    name = models.CharField(max_length=255)
    CIN = models.CharField(max_length=255, blank=True, null=True)
    first_invoice_number = models.IntegerField(default=100)
    created_by = models.ForeignKey(
        UserAccount, related_name='teams', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '%s' % self.name
