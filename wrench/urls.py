from django.conf.urls import patterns, include, url

import wrench.views

urlpatterns = patterns('',
	url(r'^$', wrench.views.ListProjectView.as_view(), name='project-list',),
	url(r'^projects/new$', wrench.views.CreateProjectView.as_view(), name='project-new',),
	url(r'^projects/(?P<pk>\d+)/$', wrench.views.ProjectView.as_view(), name='project-view',),
	url(r'^projects/(?P<pk>\d+)/plans/$', wrench.views.ListProjectPlanView.as_view(), name='project-plan-list',),
	url(r'^projects/(?P<pk>\d+)/plans/new$', wrench.views.CreateProjectPlanView.as_view(), name='project-plan-new',),
	#url(r'^$', wrench.views.ListSuiteView.as_view(), name='suite-list',),
	#url(r'^$/case', wrench.views.ListCaseView.as_view(), name='project-list',),
)