# Create your views here.

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from wrench.models import Project, Plan, Suite, Case, Run

#ListViews


class ListProjectView(ListView):

    model = Project
    template_name = "project_list.html"


class ListProjectPlanView(ListView):
    template_name = "plan_list.html"

    def get_queryset(self):
        self.project = get_object_or_404(Project, pk=self.kwargs['pk'])
        return Plan.objects.filter(project=self.project)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListProjectPlanView, self).get_context_data(**kwargs)
        # Add in the project
        context['project'] = self.project
        return context


class ListProjectSuiteView(ListView):
    model = Suite
    template_name = "suite_list.html"


class ListProjectSuiteCaseView(ListView):
    model = Case
    template_name = "case_list.html"


# DetailViews

class ProjectView(DetailView):
    model = Project
    template_name = "project_detail.html"


class PlanView(DetailView):
    model = Plan
    template_name = "plan_detail.html"


class SuiteView(DetailView):
    model = Suite
    template_name = "suite_detail.html"


class CaseView(DeleteView):
    model = Case
    template_name = "case_detail.html"

# CreateViews

class CreateProjectView(CreateView):

    model = Project
    template_name="edit_project.html"

    def get_context_data(self, **kwargs):
        context = super(CreateProjectView, self).get_context_data(**kwargs)
        context['action'] = reverse('project-new')

        return context

class CreatePlanView(CreateView):

    model = Plan
    template_name="edit_plan.html"


    def get_context_data(self, **kwargs):
        context = super(CreatePlanView, self).get_context_data(**kwargs)
        context['action'] = reverse('plan-new', kwargs={'pk': self.get_object().id})

        return context


class CreateSuiteView(CreateView):

    model = Suite    
    template_name="edit_suite.html"


    def get_context_data(self, **kwargs):
        context = super(CreateSuiteView, self).get_context_data(**kwargs)
        context['action'] = reverse('suite-new', kwargs={'pk': self.get_object().id})

        return context


class CreateCaseView(CreateView):

    model = Case
    template_name="edit_case.html"
    
    def get_context_data(self, **kwargs):
        #project = Project.objects.get(pk=self.kwargs['pk_proj'])
        #suite = Suite.objects.get(pk=self.kwargs['pk_suite'])

        context = super(CreateCaseView, self).get_context_data(**kwargs)
        context['action'] = reverse('case-new', kwargs={'pk': self.get_object().id})
 
        return context
    
# UpdateViews

class UpdateProjectView(UpdateView):

    model = Project
    template_name = "edit_project.html"

    def get_context_data(self, **kwargs):
        context = super(UpdateProjectView, self).get_context_data(**kwargs)
        context['action'] = reverse('project-edit', kwargs={'pk': self.get_object().id})

        return context

# DeleteViews

class DeleteProjectView(DeleteView):
    model = Project
    template_name = 'delete_project.html'

    def get_context_data(self, **kwargs):
        context = super(DeleteProjectView, self).get_context_data(**kwargs)
        context['action'] = reverse('project-delete', kwargs={'pk': self.get_object().id})

        return context

    def get_success_url(self):
        return reverse('project-list')

