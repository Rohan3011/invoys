from django.db import models
from accounts.models import UserAccount


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    # Corporate Identification Number
    CIN = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.TextField(blank=True, null=True)
    address2 = models.TextField(blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    country_person = models.CharField(max_length=255, blank=True, null=True)
    country_reference = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(
        UserAccount, related_name='clients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.name
