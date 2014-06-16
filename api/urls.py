from django.conf.urls import patterns, url, include

from .api import ChangeRequestList, ChangeRequestDetail
from .api import ManufacturerList, ManufacturerDetail
from .api import ConfigurationItemList, ConfigurationItemDetail

change_request_urls = patterns('',
    url(r'^$', ChangeRequestList.as_view(), name='change-list'),
)

manufacturer_urls = patterns('',
    url(r'^$', ManufacturerList.as_view(), name='manufacturer-list'),
)

config_items_urls = patterns('',
    url(r'^$', ConfigurationItemList.as_view(), name='config-item-list')
)

urlpatterns = patterns('',
    url(r'^changes', include(change_request_urls)),
    url(r'^vendors', include(manufacturer_urls)),
    url(r'^items', include(config_items_urls)),
)