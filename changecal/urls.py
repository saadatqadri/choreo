from django.conf.urls import patterns, url

urlpatterns = patterns('changecal.views',
    url(r'^changes/$', 'change_list'),
    url(r'^changes/(?P<pk>[0-9]+)/$', 'change_detail'),
)