# Create your views here.

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse

from wrench.models import Project, Plan, Suite, Case, Run

class ListProjectView(ListView):

    model = Project
    template_name = "project_list.html"

class ProjectView(DetailView):

    model = Project
    template_name = "project_detail.html"

class CreateProjectView(CreateView):

    model = Project
    template_name="edit_project.html"

    def get_context_data(self, **kwargs):
        context = super(CreateProjectView, self).get_context_data(**kwargs)
        context['action'] = reverse('project-new')

        return context


class UpdateProjectView(UpdateView):

    model = Project
    template_name = "edit_project.html"

    def get_context_data(self, **kwargs):
        context = super(UpdateProjectView, self).get_context_data(**kwargs)
        context['action'] = reverse('project-edit', kwargs={'pk': self.get_object().id})

        return context

class DeleteProjectView(DeleteView):
    model = Project
    template_name = 'delete_project.html'

    def get_context_data(self, **kwargs):
        context = super(DeleteProjectView, self).get_context_data(**kwargs)
        context['action'] = reverse('project-delete', kwargs={'pk': self.get_object().id})

        return context


class ListProjectPlanView(ListView):

    model = Plan
    template_name = "plan_list.html"


class CreateProjectPlanView(CreateView):
    model = Plan
    template_name = "edit_plan.html"


class ListSuiteView(ListView):

    model = Suite

class ListCaseView(ListView):
    
    model = Case


