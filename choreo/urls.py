from django.conf.urls import patterns, include, url
from rest_framework import routers
from changecal import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
	#url(r'^', include('changecal.urls')),
	#url(r'^api-auth/', include('rest_framework.urls', namespace="rest_framework")),
    # Examples:
    # url(r'^$', 'choreo.views.home', name='home'),
    # url(r'^choreo/', include('choreo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
