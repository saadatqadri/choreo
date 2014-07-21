from django.conf.urls import patterns, include, url

import wrench.views

urlpatterns = patterns('',
	url(r'^$', wrench.views.ListProjectView.as_view(), name='project-list',),
	url(r'^projects/(?P<pk>\d+)/$', wrench.views.ProjectView.as_view(), name='project-view',),
	url(r'^projects/(?P<pk_proj>\d+)/plans/(?P<pk>\d+)$', wrench.views.PlanView.as_view(), name='plan-view',),
	url(r'^projects/(?P<pk_proj>\d+)/suites/(?P<pk>\d+)$', wrench.views.SuiteView.as_view(), name='suite-view',),
	url(r'^projects/(?P<pk_proj>\d+)/suites/(?P<pk_suite>\d+)/cases/(?P<pk>\d+)$', wrench.views.CaseView.as_view(), name='case-view',),
	url(r'^projects/(?P<pk>\d+)/plans/$', wrench.views.ListProjectPlanView.as_view(), name='project-plan-list',),
	url(r'^projects/(?P<pk>\d+)/suites/$', wrench.views.ListProjectSuiteView.as_view(), name='project-suite-list',),
	url(r'^projects/(?P<pk_proj>\d+)/suites/(?P<pk>\d+)/cases/$', wrench.views.ListProjectSuiteCaseView.as_view(), name='project-suite-case-list',),
	url(r'^projects/new$', wrench.views.CreateProjectView.as_view(), name='project-new',),
	url(r'^projects/(?P<pk>\d+)/plans/new$', wrench.views.CreatePlanView.as_view(), name='plan-new',),
	url(r'^projects/(?P<pk>\d+)/suites/new$', wrench.views.CreateSuiteView.as_view(), name='suite-new',),
	url(r'^projects/(?P<pk_proj>\d+)/suites/(?P<pk_suite>\d+)/cases/new$', wrench.views.CreateCaseView.as_view(), name='case-new',),
	url(r'^projects/(?P<pk>\d+)/edit$', wrench.views.UpdateProjectView.as_view(), name='project-edit',),
	url(r'^projects/(?P<pk>\d+)/delete$', wrench.views.DeleteProjectView.as_view(), name='project-delete',),
	#url(r'^$', wrench.views.ListSuiteView.as_view(), name='suite-list',),
	#url(r'^$/case', wrench.views.ListCaseView.as_view(), name='project-list',),
)