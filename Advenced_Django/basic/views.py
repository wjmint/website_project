from django.db.models import fields
from django.shortcuts import render
# use it for redirect to certain url
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView, 
                                    ListView, DetailView,
                                    CreateView, UpdateView, 
                                    DeleteView)
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
    template_name = 'basic_app/school_form.html'

class SchoolDetailCreateView(CreateView):
    fields = ("name","principals","location")
    model = models.School
    template_name = 'basic_app/school_form.html'

class SchoolDeleteView(DeleteView):
    model = models.School
    context_object_name = 'school_detail'
    template_name = 'basic_app/delete_form.html'
    success_url = reverse_lazy('basic_app:list')

class StudentCreateView(CreateView):
    model = models.Student
    fields = ('name', 'age', 'school')
    template_name = 'basic_app/student_create.html'
    success_url = reverse_lazy('basic_app:detail')