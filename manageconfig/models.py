from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ('NEW', 'New'),
    ('ACTIVE', 'Active'),
    ('INACTIVE', 'Inactive'),
    ('SPARE', 'Spare'),
    ('DESTROYED', 'Destroyed'),
    ('SURPLUS', 'Surplus'),
    ('RETIRED', 'Retired-Pending Decommission'),
    ('DUPLICATE', 'Duplicate Entry'),
)

ASSET_CLASS_CHOICES = (
    ('CCA', 'CCA'),
    ('OA', 'OA'),
    ('OPA', 'OPA'),
    ('AMA', 'AMA`'),
    ('AP', 'AP'),
)

class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    service_contract_name = models.CharField(max_length=30)
    service_contract_number = models.CharField(max_length=30)
    service_contract_phone = models.CharField(max_length=30)
    service_contract_expiry = models.DateTimeField(auto_now_add=False)

    def __unicode__(self):
        return self.name

class ConfigurationItem(models.Model):
    title = models.CharField(max_length=15)
    parent = models.BooleanField(default=False)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    asset_class = models.CharField(max_length=30, choices=ASSET_CLASS_CHOICES)
    manufacturer = models.ForeignKey(Manufacturer)
    model = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    barcode = models.CharField(max_length=255)
    operating_sys = models.CharField(max_length=255)
    rack = models.CharField(max_length=25)
    description = models.TextField()
    ip = models.IPAddressField()

    def __unicode__(self):
        return self.title
