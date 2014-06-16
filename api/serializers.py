from rest_framework import serializers

from changecal.models import ChangeRequest
from manageconfig.models import Manufacturer, ConfigurationItem


class ChangeRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChangeRequest
        fields = ('id', 'title', 'created', 'status',)


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = ('id', 'name', 'service_contract_name', 'service_contract_number','service_contract_expiry',)


class ConfigurationItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConfigurationItem
        fields = ('id', 'title', 'status', 'asset_class', 'manufacturer', 'model', 'ip',)

