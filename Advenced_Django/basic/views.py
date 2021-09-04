from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView
from . import models

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    template_name = 'basic_app/school_list.html'
    context_object_name = 'schools'
    model = models.School
    