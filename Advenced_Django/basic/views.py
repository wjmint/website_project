from django.db.models import fields
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView
from . import models

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    template_name = 'basic_app/school_list.html'
    context_object_name = 'schools'
    model = models.School
    
class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School   
    template_name = 'basic_app/school_detail.html'

class SchoolDetailUpdateView(UpdateView):
    fields = ('name', 'principals')
    model = models.School

class SchoolDetailCreateView(CreateView):
    fields = ('name', 'principals', 'location')
    model = models.School

class SchoolDetailDeleteView(DeleteView):
    fields = ('name', 'principals')
    model = models.School