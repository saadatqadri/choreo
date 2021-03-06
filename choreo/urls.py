from django.conf.urls import patterns, include, url
from rest_framework import routers
from changecal import views
from django.conf import settings

from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover


urlpatterns = patterns('',
	url(r'^', include('wrench.urls')),
	#url(r'^api-auth/', include('rest_framework.urls', namespace="rest_framework")),
    # Examples:
    # url(r'^$', 'choreo.views.home', name='home'),
    # url(r'^choreo/', include('choreo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^(?P<template_name>\w+)$', SimpleStaticView.as_view(), name='choreo'),
    #url(r'^$', TemplateView.as_view(template_name='index.html')),
)


if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += patterns('',
        url(r'^(?P<path>favicon\..*)$', serve, {'document_root': settings.STATIC_ROOT}),
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], serve, {'document_root': settings.MEDIA_ROOT}),
        url(r'^%s(?P<path>.*)$' % settings.STATIC_URL[1:], 'django.contrib.staticfiles.views.serve', dict(insecure=True)),
    )
