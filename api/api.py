from rest_framework import generics, permissions

from .serializers import ChangeRequestSerializer, ManufacturerSerializer, ConfigurationItemSerializer
from changecal.models import ChangeRequest
from manageconfig.models import Manufacturer, ConfigurationItem


class ChangeRequestList(generics.ListCreateAPIView):
    model = ChangeRequest
    serializer_class = ChangeRequestSerializer
    permissions_classes = [
        permissions.AllowAny
    ]

class ChangeRequestDetail(generics.RetrieveAPIView):
    model = ChangeRequest
    serializer_class = ChangeRequestSerializer
    lookup_field = 'title'


class ManufacturerList(generics.ListCreateAPIView):
    model = Manufacturer
    serializer_class = ManufacturerSerializer
    permissions_classes = [
        permissions.AllowAny
    ]

class ManufacturerDetail(generics.RetrieveAPIView):
    model = Manufacturer
    serializer_class = ManufacturerSerializer
    lookup_field = 'name'

class ConfigurationItemList(generics.ListAPIView):
    model = ConfigurationItem
    serializer_class = ConfigurationItemSerializer
    permissions_classes = [
        permissions.AllowAny
    ]

class ConfigurationItemDetail(generics.RetrieveUpdateDestroyAPIView):
    model = ConfigurationItem
    serializer_class = ConfigurationItemSerializer
    permission_classes = [
        permissions.AllowAny
    ]
