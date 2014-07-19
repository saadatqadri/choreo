# Create your views here.

from django.views.generic import ListView, DetailView, CreateView

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


