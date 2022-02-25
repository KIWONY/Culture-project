from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView

from projectapp.forms import ProjectCreationForm
from projectapp.models import Project



class ProjectCreateView(CreateView):
    model = Project
    template_name = "projectapp/create.html"
    form_class = ProjectCreationForm

    def get_success_url(self):
        return reverse("projectapp:detail", kwargs={"pk" : self.object.pk})



class ProjectDetailView(DetailView):
    model = Project
    template_name = "projectapp/detail.html"
    context_object_name = "target_project"


class ProjectListView(ListView):
    model = Project
    template_name = "projectapp/list.html"
    context_object_name = "project_list"
    paginate_by = 5



